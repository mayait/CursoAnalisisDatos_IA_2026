# -*- coding: utf-8 -*-
"""Tomas de la serie. Cada toma es una Scene de Manim cuyo ritmo lo marcan los audios del guion.

Render de una toma: SHOT=E01-2 manim -r 1920,1080 --fps 30 serie_escenas.py Toma
El montaje de los episodios lo hace montar.py con los tiempos que esta escena escribe en tiempos/.
"""
import json
import os
import sys
import textwrap
from pathlib import Path

AQUI = Path(__file__).resolve().parent
S22 = AQUI.parent
sys.path[:0] = [str(AQUI), str(S22 / "animaciones")]

import numpy as np
from manim import *
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

import escenas as E
import guion
import voces
from escenas import AMBAR, AZUL, CLARO, GRIS, NEGRO, ROJO, T, Z, curva, df, ejes

R = json.loads((S22 / "cifras.json").read_text(encoding="utf-8"))
SHOT = os.environ.get("SHOT", "E01-0")
EP, TOMA = guion.toma_por_id(SHOT)
ILUS = S22 / "img_deck" / "ilus"
ANCHO = 14.22
BLANCO = "#FFFFFF"
coma = lambda v, d=2: f"{v:.{d}f}".replace(".", ",")
mil = lambda v: f"{v:,.0f}".replace(",", ".")


def cabe(m, ancho):
    return m.scale_to_fit_width(ancho) if m.width > ancho else m


def Zw(s, size, color=NEGRO, ancho=12.4):
    n = max(6, int(ancho / (0.0118 * size)))
    return cabe(Z("\n".join(textwrap.wrap(s, n)), size, color), ancho)


def Tw(s, size, color=NEGRO, ancho=6.0, weight=NORMAL):
    n = max(8, int(ancho / (0.0062 * size)))
    return cabe(T("\n".join(textwrap.wrap(s, n)), size, color, weight), ancho)


def etiqueta(s, fondo=NEGRO, color=BLANCO, size=22):
    t = T(s, size, color, BOLD)
    return VGroup(Rectangle(width=t.width + 0.4, height=t.height + 0.26).set_stroke(width=0).set_fill(fondo, 1).move_to(t), t)


class ConVoz:
    """Cada cue() espera a que termine la frase en curso y anota cuándo empieza la siguiente."""

    def setup(self):
        def d(b):
            p = voces.destino(b["voz"], b["texto"])
            return (voces.duracion(p) if p.exists() else 1.4 if os.environ.get("SIN_AUDIO") else voces.duracion(p)) + b.get("pausa", 0) * (0 if os.environ.get("SIN_AUDIO") else 1) + 0.4
        self.durs = [d(b) for b in TOMA["beats"]]
        self.k, self.t0, self.inicios = 0, 0.0, []
        if TOMA.get("titulo"):
            t_ = cabe(Z(TOMA["titulo"].upper(), 34), 13.0).move_to([-6.5, 3.42, 0], aligned_edge=LEFT)
            self.add_fixed_in_frame_mobjects(t_) if isinstance(self, ThreeDScene) else self.add(t_)

    def wait(self, duration=1.0, **kw):
        super().wait(min(duration, 0.12), **kw)

    def cue(self):
        falta = self.durs[self.k] - (self.renderer.time - self.t0)
        if falta > 1 / 30:
            super().wait(falta)
        self.inicios.append(self.t0)
        self.k += 1
        self.t0 = self.renderer.time

    def tear_down(self):
        assert self.k == len(self.durs), f"{SHOT}: {self.k} cues para {len(self.durs)} beats"
        (AQUI / "tiempos").mkdir(exist_ok=True)
        (AQUI / "tiempos" / f"{SHOT}.json").write_text(json.dumps({"inicios": self.inicios, "dur": self.renderer.time}))


# ---------------------------------------------------------------- portadas e ilustraciones
def portada(s):
    s.camera.background_color = ROJO
    tag = etiqueta(f"EPISODIO {TOMA['n']}").move_to([-6.5, 2.55, 0], aligned_edge=LEFT)
    tit = Zw(EP["titulo"].upper(), 80, BLANCO, 12.8).next_to(tag, DOWN, buff=0.4, aligned_edge=LEFT)
    serie = T("Una recta no se dobla", 34, BLANCO, BOLD).move_to([-6.5, -2.2, 0], aligned_edge=LEFT)
    pie = VGroup(Z("WE WANT MORE", 24, BLANCO), etiqueta("EVIDENCE", NEGRO, BLANCO, 22)).arrange(RIGHT, buff=0.2).move_to([-6.5, -3.35, 0], aligned_edge=LEFT)
    s.play(FadeIn(tag, shift=RIGHT * 0.4), FadeIn(tit, shift=RIGHT * 0.8), run_time=0.8)
    s.play(FadeIn(serie), FadeIn(pie), run_time=0.4)
    s.cue()


def ilus(s):
    img = ImageMobject(str(ILUS / f"{TOMA['img']}.jpg"))
    img.height = 8.3
    img.move_to([ANCHO / 2 - img.width / 2 + 0.05, 0, 0])
    izq = img.get_left()[0]
    borde = Rectangle(width=izq + ANCHO / 2 + 0.3, height=8.5).set_stroke(width=0).set_fill(BLANCO, 1).move_to([(-ANCHO / 2 - 0.3 + izq) / 2, 0, 0]).set_z_index(3)
    centro = img.get_center()
    img.add_updater(lambda m, dt: m.scale(1 + 0.008 * dt, about_point=centro))
    s.add(img, borde)
    margen, disp = -6.5, izq + 6.5 - 0.4
    actual = None
    for b in TOMA["beats"]:
        lineas = b["rotulo"].split("\n")
        size = min(88, disp / (max(map(len, lineas)) * 0.0097))
        grupo = VGroup(cabe(Z(b["rotulo"].upper(), size, ROJO if b["rotulo"][0].isdigit() else NEGRO), disp))
        if b["voz"] != "narrador":
            grupo.add(etiqueta(b["voz"].upper(), ROJO))
            grupo.arrange(UP, buff=0.3, aligned_edge=LEFT)
        grupo.move_to([margen, 0, 0], aligned_edge=LEFT).set_z_index(4)
        if actual is not None:
            s.play(FadeOut(actual, shift=UP * 0.25), FadeIn(grupo, shift=UP * 0.25), run_time=0.45)
        else:
            s.play(FadeIn(grupo, shift=UP * 0.25), run_time=0.5)
        actual = grupo
        s.cue()


def apuesta(s):
    s.camera.background_color = ROJO
    img = ImageMobject(str(ILUS / "apuesta.jpg"))
    img.height = 8.3
    img.move_to([ANCHO / 2 - img.width / 2 + 0.05, 0, 0])
    tag = etiqueta("APUESTA").move_to([-6.5, 2.7, 0], aligned_edge=LEFT)
    tx = Zw("20 MERCADOS YA INVIERTEN PARECIDO A SU PLAN", 46, BLANCO, 7.6).move_to([-6.5, 0.95, 0], aligned_edge=LEFT)
    s.add(img)
    s.play(FadeIn(tag), FadeIn(tx, shift=UP * 0.2))
    s.cue()
    q = T("¿Cuánto venden en promedio?", 40, BLANCO, BOLD).move_to([-6.5, -1.05, 0], aligned_edge=LEFT)
    sub = T("En miles de unidades. Pausa y escríbelo.", 28, BLANCO).move_to([-6.5, -1.75, 0], aligned_edge=LEFT)
    s.play(FadeIn(q), FadeIn(sub))
    s.cue()
    fondo = Rectangle(width=ANCHO + 1, height=9).set_stroke(width=0).set_fill(BLANCO, 1).set_z_index(5)
    a = VGroup(Z("12,43", 130, GRIS), T("les pronostica el plano", 34)).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to([-6.3, 0.7, 0], aligned_edge=LEFT).set_z_index(6)
    b = VGroup(Z("10,16", 130, ROJO), T("vendieron de verdad", 34)).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to([0.6, 0.7, 0], aligned_edge=LEFT).set_z_index(6)
    s.play(FadeIn(fondo), FadeIn(a, shift=UP * 0.3))
    s.cue()
    s.play(FadeIn(b, shift=UP * 0.3))
    s.cue()
    c = T("2.270 unidades de más por mercado, en promedio.", 40, NEGRO, BOLD).move_to([-6.3, -2.3, 0], aligned_edge=LEFT).set_z_index(6)
    s.play(FadeIn(c, shift=UP * 0.2))
    s.cue()


# ---------------------------------------------------------------- mapas de error
X_ = np.column_stack([np.ones(len(df)), df.tv, df.radio])
X2 = np.column_stack([X_, df.tv * df.radio, df.tv ** 2])
RES1 = df.ventas.values - X_ @ np.linalg.lstsq(X_, df.ventas.values, rcond=None)[0]
RES2 = df.ventas.values - X2 @ np.linalg.lstsq(X2, df.ventas.values, rcond=None)[0]
LUZ = ManimColor("#EDEDED")


def tono(r):
    t = float(np.clip(r / 5, -1, 1))
    return interpolate_color(LUZ, ManimColor(ROJO if t < 0 else AZUL), abs(t) ** 0.7)


def pintar(dots, de, a):
    return UpdateFromAlphaFunc(dots, lambda g, al: [d.set_color(interpolate_color(ManimColor(c0), ManimColor(c1), al)) for d, c0, c1 in zip(g, de, a)], run_time=1.6)


def mapa_ejes():
    g, ax = ejes((0, 300), (0, 52), 11.8, 4.9, "Inversión en TV (miles de USD)", "Inversión en radio (miles de USD)", (0, 100, 200, 300), (0, 25, 50))
    g.move_to([-0.4, -0.55, 0])
    return g, ax


def rot(t, pos, color):
    m = T(t, 26, color, BOLD).move_to(pos)
    m.add_background_rectangle(color=WHITE, opacity=0.86)
    return m


def mapa(s):
    g, ax = mapa_ejes()
    dots = VGroup(*[Dot(ax.c2p(a, b), radius=0.1, color=CLARO) for a, b in zip(df.tv, df.radio)])
    s.play(Create(g), run_time=0.8)
    s.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.006), run_time=1.6)
    s.cue()
    s.play(pintar(dots, [CLARO] * len(dots), [tono(r) for r in RES1]))
    s.cue()
    a = rot("Solo radio: promete de más", ax.c2p(58, 22), ROJO)
    b = rot("Solo TV: promete de más", ax.c2p(248, 21), ROJO)
    s.play(FadeIn(a), FadeIn(b))
    s.cue()
    c = rot("Los dos medios: se queda corto", ax.c2p(232, 40), AZUL)
    s.play(FadeIn(c))
    s.cue()
    p = ax.c2p(50, 49)
    x = VGroup(Line(p + UL * 0.2, p + DR * 0.2, stroke_width=11, color=NEGRO), Line(p + UR * 0.2, p + DL * 0.2, stroke_width=11, color=NEGRO))
    et = rot("El plan de Daniela", ax.c2p(101, 49.5), NEGRO)
    s.play(GrowFromCenter(x), FadeIn(et))
    s.cue()


def antesdespues(s):
    g, ax = ejes((0, 300), (0, 52), 10.0, 4.9, "Inversión en TV (miles de USD)", "Inversión en radio (miles de USD)", (0, 100, 200, 300), (0, 25, 50))
    g.move_to([-1.55, -0.55, 0])
    c0, c1 = [tono(r) for r in RES1], [tono(r) for r in RES2]
    dots = VGroup(*[Dot(ax.c2p(a, b), radius=0.1, color=c0[i]) for i, (a, b) in enumerate(zip(df.tv, df.radio))])
    n = ValueTracker(R["errores_grandes"]["plano_n_mayor_2"])
    cont = always_redraw(lambda: VGroup(Z(f"{int(round(n.get_value()))}", 96, ROJO), Tw("mercados con error mayor a 2 mil", 24, GRIS, 2.7)).arrange(DOWN, buff=0.2).move_to([5.3, 0, 0]))
    nom = T("Plano", 34, NEGRO, BOLD).move_to([5.3, 2.05, 0])
    s.play(Create(g), FadeIn(dots), FadeIn(cont), FadeIn(nom))
    s.cue()
    nom2 = T("Plano doblado", 30, NEGRO, BOLD).move_to([5.3, 2.05, 0])
    s.play(pintar(dots, c0, c1), n.animate.set_value(R["errores_grandes"]["curva_n_mayor_2"]), FadeOut(nom), FadeIn(nom2), run_time=2.4)
    s.cue()
    s.play(Indicate(cont, color=AZUL, scale_factor=1.06))
    s.cue()


# ---------------------------------------------------------------- barras y curvas
def barra(x, valor, escala, ancho, color, base=-2.95):
    return Rectangle(width=ancho, height=max(valor * escala, 0.01)).set_stroke(width=0).set_fill(color, 1).move_to([x, base + valor * escala / 2, 0])


def crece(b, base=-2.95):
    return GrowFromEdge(b, DOWN)


def escalera(s):
    e = R["escalera"]
    v = [R["mae_base"], e["plano"]["mae_te"], e["interaccion"]["mae_te"], e["curva"]["mae_te"]]
    et, col = ["Promedio", "TV + radio", "+ TV × radio", "+ TV²"], [CLARO, GRIS, "#F08A8E", ROJO]
    xs = [-4.9, -1.6, 1.7, 5.0]
    esc = 1.0
    linea = Line([-6.6, -2.95, 0], [6.6, -2.95, 0], color=CLARO, stroke_width=3)
    s.add(linea)
    for i in range(4):
        b = barra(xs[i], v[i], esc, 2.2, col[i])
        n = Z(coma(v[i]), 48).next_to(b, UP, buff=0.14)
        l = T(et[i], 30).move_to([xs[i], -3.4, 0])
        s.play(crece(b), FadeIn(n), FadeIn(l), run_time=0.9)
        if i == 1:
            tol = DashedLine([-6.6, -0.95, 0], [6.6, -0.95, 0], color=NEGRO, stroke_width=3)
            tt = T("Tolerancia de Daniela: 2", 24).move_to([5.3, -0.7, 0])
            s.play(Create(tol), FadeIn(tt), run_time=0.6)
        s.cue()


def radiotv(s):
    b = R["curva_200"]
    f = lambda t: (b["radio"] + b["tv:radio"] * t) * 1000 * 12 - 1000
    g, ax = ejes((0, 300), (-1000, 3400), 11.6, 4.9, "Lo que ese mercado ya invierte en TV (miles de USD)", "Ganancia por cada 1.000 USD más en radio (USD)", (0, 100, 200, 300), (-1000, 0, 1000, 2000, 3000), fmt=lambda v: mil(v))
    g.move_to([0, -0.55, 0])
    cero = Line(ax.c2p(0, 0), ax.c2p(300, 0), color=NEGRO, stroke_width=2)
    s.play(Create(g), Create(cero), run_time=1)
    s.cue()
    gp = R["plano_ganancia"]["radio"]
    pl = DashedLine(ax.c2p(0, gp), ax.c2p(296, gp), color=GRIS, stroke_width=5)
    tp = rot("Lo que decía el plano", ax.c2p(240, gp + 280), GRIS)
    s.play(Create(pl), FadeIn(tp))
    s.cue()
    prev = 0
    for t in (50, 150, 250):
        l = Line(ax.c2p(prev, f(prev)), ax.c2p(t, f(t)), color=ROJO, stroke_width=8)
        d = Dot(ax.c2p(t, f(t)), radius=0.14, color=ROJO)
        n = rot(("+" if f(t) > 0 else "") + mil(f(t)) + " USD", ax.c2p(t - 24, f(t) + 400), ROJO)
        s.play(Create(l), run_time=1.0, rate_func=linear)
        s.play(GrowFromCenter(d), FadeIn(n), run_time=0.4)
        prev = t
        s.cue()
    eq = R["radio_equilibrio_tv"]
    d = Dot(ax.c2p(eq, 0), radius=0.14, color=NEGRO)
    txt = rot("Se paga desde 45 mil en TV", ax.c2p(112, -620), NEGRO)
    zona = Polygon(ax.c2p(0, f(0)), ax.c2p(eq, 0), ax.c2p(0, 0)).set_stroke(width=0).set_fill(ROJO, 0.22)
    s.play(FadeIn(zona), GrowFromCenter(d), FadeIn(txt))
    s.cue()


def promesacorr(s):
    pb, pa = R["planes"]["daniela"], R["planes"]["agencia"]
    v = ValueTracker(pb["plano"] * 1000)
    num = always_redraw(lambda: Z(mil(round(v.get_value(), -1)), 118, ROJO).move_to([-6.4, 1.1, 0], aligned_edge=LEFT))
    et = T("Plan de Daniela · unidades", 30, GRIS).move_to([-6.4, 2.25, 0], aligned_edge=LEFT)
    s.play(FadeIn(num), FadeIn(et))
    s.cue()
    s.play(v.animate.set_value(pb["curva"] * 1000), run_time=3, rate_func=smooth)
    s.cue()
    tag = etiqueta("2.650 unidades de más", ROJO, BLANCO, 30).move_to([-6.4, -0.2, 0], aligned_edge=LEFT)
    s.play(FadeIn(tag, shift=UP * 0.2))
    s.cue()
    ag = VGroup(T("Agencia · unidades", 28, GRIS), Z(mil(round(pa["curva"] * 1000, -1)), 58), T("+76 mil USD de inversión", 26)).arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to([2.3, 1.1, 0], aligned_edge=LEFT)
    s.play(FadeIn(ag, shift=LEFT * 0.3))
    s.cue()
    esc = 0.11
    fila = lambda y, nom, val, color: VGroup(T(nom, 30).move_to([-4.9, y, 0], aligned_edge=LEFT), Rectangle(width=val * esc, height=0.5).set_stroke(width=0).set_fill(color, 1).move_to([-2.5, y, 0], aligned_edge=LEFT))
    f1, f2 = fila(-1.6, "Daniela", pb["utilidad_curva"], ROJO), fila(-2.4, "Agencia", pa["utilidad_curva"], GRIS)
    n1 = Z("+" + coma(pb["utilidad_curva"], 1) + " mil USD", 34, ROJO).next_to(f1[1], RIGHT, buff=0.2)
    n2 = Z("+" + coma(pa["utilidad_curva"], 1) + " mil USD", 34, GRIS).next_to(f2[1], RIGHT, buff=0.2)
    u = T("Utilidad", 24, GRIS).move_to([-6.4, -2.0, 0], aligned_edge=LEFT)
    s.play(FadeIn(u), FadeIn(f1[0]), GrowFromEdge(f1[1], LEFT), FadeIn(n1), FadeIn(f2[0]), GrowFromEdge(f2[1], LEFT), FadeIn(n2), run_time=1.2)
    s.cue()
    fin = Z("LA DECISIÓN SE SOSTIENE. LA CIFRA NO", 34, NEGRO).move_to([0, -3.4, 0])
    s.play(FadeIn(fin, shift=UP * 0.2))
    s.cue()


def grados(s):
    G = R["grados"]
    x = [g["grado"] for g in G]
    g1, a1 = ejes((1, 7), (0.88, 1.0), 5.6, 4.5, "Grado", "R² en entrenamiento", x, (0.9, 1.0), fmt=lambda v: str(v) if isinstance(v, int) else coma(v, 1))
    g1.move_to([-3.7, -0.55, 0])
    lg = lambda v: np.log10(v)
    g2, a2 = ejes((1, 7), (lg(0.07), lg(60)), 5.6, 4.5, "Grado", "Error medio, escala logarítmica", x, (), fmt=str)
    g2.move_to([3.5, -0.55, 0])
    for v, t in ((0.1, "0,1"), (1, "1"), (10, "10")):
        g2.add(T(t, 22, GRIS).next_to(a2.c2p(1, lg(v)), LEFT, buff=0.14))
    linea = lambda ax, f, i, j, c, w: VGroup(*[Line(ax.c2p(x[k], f(G[k])), ax.c2p(x[k + 1], f(G[k + 1])), color=c, stroke_width=w) for k in range(i, j)])
    fr, fe = lambda g: g["r2_tr"], lambda g: lg(g["mae_te"])
    s.play(FadeIn(g1), FadeIn(g2), run_time=0.7)
    s.play(Create(linea(a1, fr, 0, 6, NEGRO, 7)), run_time=2.4, rate_func=linear)
    s.play(FadeIn(T(coma(G[-1]["r2_tr"], 3), 34, NEGRO, BOLD).next_to(a1.c2p(7, G[-1]["r2_tr"]), DOWN + LEFT, buff=0.12)))
    s.cue()
    s.play(Create(linea(a2, lambda g: lg(g["mae_tr"]), 0, 6, GRIS, 5)), run_time=1)
    s.play(Create(linea(a2, fe, 0, 2, ROJO, 8)), run_time=1.1, rate_func=linear)
    s.cue()
    s.play(Create(linea(a2, fe, 2, 5, ROJO, 8)), run_time=1.6, rate_func=linear)
    s.play(FadeIn(rot("3,25", a2.c2p(5.3, lg(5.6)), ROJO)))
    s.cue()
    s.play(Create(linea(a2, fe, 5, 6, ROJO, 8)), run_time=0.8, rate_func=linear)
    s.play(FadeIn(rot("42,9", a2.c2p(6.0, lg(38)), ROJO)))
    s.cue()


def mercado(s):
    C = ["tv", "radio", "prensa"]
    tr, te = train_test_split(df, test_size=0.25, random_state=42)
    p = make_pipeline(PolynomialFeatures(6, include_bias=False), StandardScaler(), LinearRegression()).fit(tr[C], tr.ventas)
    te = te.assign(pred=p.predict(te[C])).sort_values("ventas").reset_index(drop=True)
    g, ax = ejes((0, 49), (-105, 32), 12.4, 5.0, "Los 50 mercados de prueba, de menor a mayor venta real", "Ventas (miles)", (), (-100, -50, 0), fmt=lambda v: str(v).replace("-", "−"))
    g.move_to([0, -0.5, 0])
    cero = DashedLine(ax.c2p(0, 0), ax.c2p(49, 0), color=CLARO)
    s.play(Create(g), Create(cero), run_time=0.8)
    reales = VGroup(*[Dot(ax.c2p(i, v), radius=0.08, color=NEGRO) for i, v in enumerate(te.ventas)])
    s.play(LaggedStart(*[GrowFromCenter(d) for d in reales], lag_ratio=0.03), run_time=1.5)
    s.cue()
    k = int(te.index[te.mercado == R["grado6"]["peor_mercado"]][0])
    pr = VGroup(*[Circle(radius=0.08, color=ROJO, stroke_width=3).move_to(ax.c2p(i, max(v, -12) if i != k else te.ventas[k])) for i, v in enumerate(te.pred)])
    s.play(LaggedStart(*[FadeIn(c, scale=0.5) for c in pr], lag_ratio=0.02), run_time=1.5)
    s.cue()
    s.play(Flash(reales[k], color=ROJO, flash_radius=0.4), reales[k].animate.scale(1.8), run_time=0.9)
    s.cue()
    y0, y1 = te.ventas[k], te.pred[k]
    s.play(Create(Line(ax.c2p(k, y0), ax.c2p(k, y1), color=ROJO, stroke_width=5)), pr[k].animate.move_to(ax.c2p(k, y1)), run_time=1.3, rate_func=rush_into)
    t = rot("Mercado 17: pronostica −98 mil. Vendió 12,5 mil.", ax.c2p(k + 12 if k < 26 else k - 13, y1 + 22), ROJO)
    s.play(FadeIn(t))
    s.cue()


# ---------------------------------------------------------------- freno
def caja(x, ancho, fondo, color, grande, chico):
    r = Rectangle(width=ancho, height=2.2).set_stroke(width=0).set_fill(fondo, 1).move_to([x, 0.8, 0])
    return VGroup(r, cabe(Z(grande, 44 if len(grande) > 2 else 76, color), ancho - 0.3).move_to([x, 1.15, 0]), cabe(T(chico, 24, color), ancho - 0.3).move_to([x, 0.15, 0]))


def freno(s):
    a = caja(-4.95, 3.3, "#F0F0F0", NEGRO, "ERROR", "lo que ya minimizábamos")
    b = caja(-0.85, 2.0, ROJO, BLANCO, "λ", "fuerza del freno")
    c = caja(3.95, 5.0, NEGRO, BLANCO, "TAMAÑO DE LOS b", "cuánto se apoya en cada columna")
    mas, por = T("+", 70, NEGRO, BOLD).move_to([-2.7, 0.8, 0]), T("×", 70, NEGRO, BOLD).move_to([0.75, 0.8, 0])
    s.play(FadeIn(a, shift=UP * 0.3))
    s.cue()
    s.play(FadeIn(mas), FadeIn(b, shift=UP * 0.3), FadeIn(por), FadeIn(c, shift=UP * 0.3))
    s.cue()
    s.play(Indicate(b, color=NEGRO, scale_factor=1.12), run_time=1)
    s.cue()
    lin = Line([-5.4, -1.85, 0], [5.4, -1.85, 0], color=CLARO, stroke_width=10)
    k = Circle(radius=0.26, color=ROJO, fill_opacity=1).move_to([-5.4, -1.85, 0])
    t0 = T("λ = 0: sin freno", 30, NEGRO, BOLD).move_to([-6.4, -2.75, 0], aligned_edge=LEFT)
    s.play(FadeIn(lin), FadeIn(k), FadeIn(t0))
    s.cue()
    t1 = T("λ enorme: el promedio", 30, NEGRO, BOLD).move_to([6.4, -2.75, 0], aligned_edge=RIGHT)
    s.play(k.animate.move_to([5.4, -1.85, 0]), FadeIn(t1), run_time=1.6)
    s.play(k.animate.move_to([0, -1.85, 0]), run_time=1.2)
    s.play(FadeIn(T("la respuesta está en el medio", 26, ROJO, BOLD).move_to([0, -1.2, 0])))
    s.cue()


def escala(s):
    def tarjeta(x, sub, b_txt):
        r = Rectangle(width=6.1, height=2.5).set_stroke(width=0).set_fill("#F0F0F0", 1).move_to([x, 1.2, 0])
        return VGroup(r, T(sub, 28, GRIS).move_to([x - 2.75, 2.05, 0], aligned_edge=LEFT), Z(b_txt, 48).move_to([x - 2.75, 1.05, 0], aligned_edge=LEFT))
    a, b = tarjeta(-3.3, "TV en miles de USD", "b = 0,0458"), tarjeta(3.3, "La misma TV, en USD", "b = 0,0000458")
    s.play(FadeIn(a, shift=UP * 0.2))
    s.cue()
    s.play(FadeIn(b, shift=UP * 0.2))
    s.cue()
    t = Tw("Mismo pronóstico, otro cobro: el freno castigaría la unidad, no la variable.", 36, NEGRO, 12.6, BOLD).move_to([0, -1.05, 0])
    s.play(FadeIn(t, shift=UP * 0.2))
    s.cue()
    u = Z("MEDIA 0 · DESVIACIÓN 1", 48, ROJO).move_to([0, -2.7, 0])
    s.play(FadeIn(u, shift=UP * 0.2))
    s.cue()


def rejilla(s):
    L = R["rejilla"]["lasso"]
    xs = [-5.8 + i * 1.45 for i in range(len(L))]
    base = -0.15
    esc = 0.05
    et = VGroup(*[T(coma(l["alpha"], 4).rstrip("0").rstrip(",") if l["alpha"] < 1 else "1", 22, GRIS).move_to([xs[i], -3.45, 0]) for i, l in enumerate(L)])
    s.add(T("Columnas que sobreviven, de 55", 26, GRIS).move_to([-6.5, 2.55, 0], aligned_edge=LEFT))
    s.play(FadeIn(et), FadeIn(T("Fuerza del freno α", 22, GRIS).move_to([5.6, -3.0, 0])), run_time=0.3)
    barras = []
    for i, l in enumerate(L):
        b = barra(xs[i], l["vivas"], esc, 0.9, GRIS, base)
        n = Z(str(l["vivas"]), 34).next_to(b, UP, buff=0.08)
        barras.append((b, n))
        s.play(crece(b), FadeIn(n), run_time=0.28)
    s.cue()
    mx = 1.15
    py = lambda v: -3.1 + (v - 0.3) / (mx - 0.3) * 2.3
    t = T("Error en validación cruzada", 24, GRIS).move_to([-6.5, -0.55, 0], aligned_edge=LEFT)
    pts = [[xs[i], py(l["cv_mae"]), 0] for i, l in enumerate(L)]
    lin = VMobject(stroke_color=ROJO, stroke_width=7).set_points_as_corners(pts)
    s.play(FadeIn(t), Create(lin), run_time=1.6, rate_func=linear)
    m = int(np.argmin([l["cv_mae"] for l in L]))
    an = Circle(radius=0.26, color=NEGRO, stroke_width=4).move_to(pts[m])
    s.play(Create(an), Indicate(barras[m][1], color=ROJO))
    s.cue()
    s.play(barras[7][0].animate.set_fill(ROJO, 1), Indicate(barras[7][1], color=ROJO, scale_factor=1.4))
    txt = etiqueta("tv  y  tv × radio", ROJO, BLANCO, 32).move_to([xs[7] - 1.2, 1.2, 0])
    s.play(FadeIn(txt, shift=UP * 0.2))
    s.cue()
    s.play(Indicate(txt, color=NEGRO, scale_factor=1.08), run_time=1)
    s.cue()


def final(s):
    e, g5, rj = R["escalera"], R["grados"][4], R["rejilla"]
    it = [("Plano", 2, e["plano"]["mae_te"], GRIS), ("Grado 5\nsin freno", 55, g5["mae_te"], CLARO), ("Grado 5\ncon Ridge", 55, rj["ridge_mejor"]["mae_te"], "#F08A8E"),
          ("Grado 5\ncon Lasso", rj["lasso_mejor"]["vivas"], rj["lasso_mejor"]["mae_te"], "#F08A8E"), ("Curva\ncon TV²", 4, e["curva"]["mae_te"], NEGRO), ("Curva\ncon √TV", 4, e["raiz_tv"]["mae_te"], ROJO)]
    n = 6 if TOMA["conraiz"] else 5
    xs = np.linspace(-5.4, 5.4, n)
    esc = 2.65
    s.add(Line([-6.6, -2.6, 0], [6.6, -2.6, 0], color=CLARO, stroke_width=3))
    def uno(i):
        nom, col, v, c = it[i]
        b = barra(xs[i], v, esc, 1.5, c, -2.6)
        tx = VGroup(Z(coma(v), 40), T(f"{col} columnas", 20, GRIS)).arrange(UP, buff=0.08).next_to(b, UP, buff=0.1)
        return crece(b), FadeIn(tx), FadeIn(T(nom, 24).move_to([xs[i], -3.2, 0])), b
    if not TOMA["conraiz"]:
        for g in ((0,), (1,), (2, 3), (4,)):
            s.play(*[a for i in g for a in uno(i)[:3]], run_time=0.9)
            s.cue()
        s.play(Circumscribe(VGroup(Dot([xs[4], -2.6, 0]), Dot([xs[4], -0.9, 0])), color=ROJO, buff=0.9), run_time=1.4)
        s.cue()
    else:
        s.play(*[a for i in range(5) for a in uno(i)[:3]], run_time=1)
        s.cue()
        ul = uno(5)
        s.play(*ul[:3], run_time=1)
        s.cue()
        s.play(Circumscribe(ul[3], color=NEGRO, buff=0.15), run_time=1.4)
        s.cue()


def raiz(s):
    ec, er = R["escalera"]["curva"], R["escalera"]["raiz_tv"]
    b_ = df[df.radio <= 12]
    rm = b_.radio.mean()
    xs = np.linspace(0.7, 296, 240)
    yc = ec["intercepto"] + ec["coef"]["tv"] * xs + ec["coef"]["radio"] * rm + ec["coef"]["tv_radio"] * xs * rm + ec["coef"]["tv2"] * xs ** 2
    yr = er["intercepto"] + er["coef"]["tv"] * xs + er["coef"]["raiz_tv"] * np.sqrt(xs) + er["coef"]["radio"] * rm + er["coef"]["tv_radio"] * xs * rm
    g, ax = ejes((0, 300), (0, 16), 12.2, 5.0, "TV (miles de USD), mercados con poca radio", "Ventas (miles)", (0, 100, 200, 300), (0, 5, 10, 15))
    g.move_to([0, -0.5, 0])
    s.play(Create(g), LaggedStart(*[GrowFromCenter(Dot(ax.c2p(a, b), radius=0.08, color=NEGRO)) for a, b in zip(b_.tv, b_.ventas)], lag_ratio=0.01), run_time=1.4)
    c1 = curva(ax, xs, yc, 0, 16, GRIS, 6)
    s.play(Create(c1), run_time=1.6)
    s.play(FadeIn(rot("Con TV²: arranca demasiado alta", ax.c2p(205, 6.2), GRIS)))
    s.cue()
    c2 = curva(ax, xs, yr, 0, 16, ROJO, 7)
    s.play(Create(c2), run_time=2)
    s.play(FadeIn(rot("Con √TV: sube rápido y se aplana", ax.c2p(85, 14.5), ROJO)))
    s.cue()


def co2(s):
    m = R["co2"]["mitades"]
    filas = [("FUELCONSUMPTION_COMB", "Consumo combinado"), ("FUELCONSUMPTION_HWY", "Consumo carretera"), ("FUELCONSUMPTION_CITY", "Consumo ciudad")]
    g, ax = ejes((-140, 210), (0, 3), 9.4, 4.8, "Rango del coeficiente en seis mitades distintas de los datos", "", (-100, 0, 100, 200), (), fmt=lambda v: str(v).replace("-", "−"))
    g.move_to([2.0, -0.55, 0])
    s.add(g, DashedLine(ax.c2p(0, 0), ax.c2p(0, 3), color=CLARO))
    for i, (_, n) in enumerate(filas):
        s.add(T(n, 26).next_to(ax.c2p(-140, 2.5 - i), LEFT, buff=0.2))
    def pasar(nom, dy, color, ancho, extra):
        anims = []
        for i, (c, _) in enumerate(filas):
            lo, hi = m[nom][c]
            y = 2.5 - i + dy
            if hi - lo < 1:
                anims.append(GrowFromCenter(Dot(ax.c2p(lo, y), radius=0.11, color=color)))
            else:
                anims.append(GrowFromPoint(Line(ax.c2p(lo, y), ax.c2p(hi, y), color=color, stroke_width=ancho), ax.c2p((lo + hi) / 2, y)))
        s.play(*anims, FadeIn(extra), run_time=1.3)
        s.cue()
    pasar("ols", -0.26, GRIS, 12, rot("Sin freno: de −87 a +198", ax.c2p(120, 1.65), GRIS))
    pasar("ridge", 0, ROJO, 12, rot("Ridge: quieto", ax.c2p(70, 0.95), ROJO))
    pasar("lasso", 0.26, NEGRO, 12, rot("Lasso: unas sí y otras no", ax.c2p(130, 0.35), NEGRO))


def guia(s):
    for i, (a, b) in enumerate(TOMA["filas"]):
        y = 1.95 - i * 1.15
        l = T(a, 30).move_to([-6.4, y, 0], aligned_edge=LEFT)
        r = T(b, 30, ROJO, BOLD).move_to([1.6, y, 0], aligned_edge=LEFT)
        s.play(FadeIn(l, shift=RIGHT * 0.2), run_time=0.4)
        s.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.4)
        s.cue()


def ejercicio(s):
    tag = etiqueta(f"EJERCICIO · ETAPA {TOMA['etapa']}", ROJO).move_to([-6.5, 3.5, 0], aligned_edge=LEFT)
    tit = cabe(Z(TOMA["nombre"].upper(), 44), 9.0).next_to(tag, RIGHT, buff=0.4)
    s.add(tag, tit)
    q = VGroup(etiqueta("DANIELA", NEGRO, BLANCO, 20), Tw(TOMA["beats"][0]["rotulo"], 30, NEGRO, 10.9, BOLD)).arrange(RIGHT, buff=0.3, aligned_edge=UP).move_to([-6.5, 2.5, 0], aligned_edge=LEFT)
    s.play(FadeIn(q, shift=UP * 0.2))
    s.cue()
    panel = Rectangle(width=6.7, height=4.1).set_stroke(width=0).set_fill("#141414", 1).move_to([3.4, -0.6, 0])
    s.play(FadeIn(panel), run_time=0.4)
    codigo = None
    y = 1.0
    for i, p in enumerate(TOMA["pasos"]):
        if p is None:
            pa = VGroup(Rectangle(width=2.9, height=1.0).set_stroke(width=0).set_fill(ROJO, 1), Z("PAUSA", 44, BLANCO)).move_to([-4.75, -3.05, 0])
            s.play(GrowFromCenter(pa), Indicate(q, color=NEGRO, scale_factor=1.02), run_time=0.7)
            s.cue()
            continue
        texto, cod = p
        num = Z(str(i + 1), 56, ROJO).move_to([-6.2, y - 0.2, 0])
        tx = Tw(texto, 27, NEGRO, 5.1).move_to([-5.55, y - 0.2, 0], aligned_edge=LEFT)
        y -= 1.33
        nuevo = Text(cod, font="Menlo", font_size=25, color=BLANCO, line_spacing=0.9).move_to([0.3, -0.6, 0], aligned_edge=LEFT)
        if nuevo.width > 6.3:
            nuevo.scale_to_fit_width(6.3).move_to([0.3, -0.6, 0], aligned_edge=LEFT)
        if codigo is not None:
            s.play(FadeOut(codigo), run_time=0.25)
        s.play(FadeIn(num), FadeIn(tx, shift=RIGHT * 0.2), run_time=0.45)
        s.play(AddTextLetterByLetter(nuevo, time_per_char=0.018))
        codigo = nuevo
        s.cue()


def cierre(s):
    img = ImageMobject(str(ILUS / "decision.jpg"))
    img.height = 8.3
    img.move_to([ANCHO / 2 - img.width / 2 + 0.05, 0, 0])
    a = cabe(Text("MORE\nEVIDENCE,", font=E.TITULO, font_size=92, color=NEGRO), 7.4).move_to([-6.4, 1.3, 0], aligned_edge=LEFT)
    b = cabe(Z("MORE\nDRAGONS.", 92, ROJO), 7.4).move_to([-6.4, -1.15, 0], aligned_edge=LEFT)
    pie = T("USFQ | GALÁPAGOS · ADM 2003 ANÁLISIS DE DATOS", 22, NEGRO, BOLD).move_to([-6.4, -3.45, 0], aligned_edge=LEFT)
    s.add(img)
    s.play(FadeIn(a, shift=UP * 0.2), run_time=0.8)
    s.play(FadeIn(b, shift=UP * 0.2), FadeIn(pie), run_time=0.8)
    s.cue()


# ---------------------------------------------------------------- sub-videos de interacciones
RI = json.loads((AQUI / "cifras_inter.json").read_text(encoding="utf-8"))
M, PL = RI["modelo"], RI["plano"]
f_inter = lambda t, r: M["Intercept"] + M["tv"] * t + M["radio"] * r + M["tv:radio"] * t * r
f_plano = lambda t, r: PL["Intercept"] + PL["tv"] * t + PL["radio"] * r
RS = df.radio.values


def grad(r):
    return interpolate_color(ManimColor(NEGRO), ManimColor(ROJO), float(np.clip(r / 50, 0, 1)))


def col_corte(r, a, c):
    return ManimColor(ROJO) if r >= c else ManimColor(NEGRO) if r <= a else ManimColor(CLARO)


def separar(s):
    g, ax = ejes((0, 300), (0, 30), 8.6, 4.9, "TV (miles de USD)", "Ventas (miles)", (0, 100, 200, 300), (0, 10, 20, 30))
    g.move_to([-2.5, -0.55, 0])
    dots = VGroup(*[Dot(ax.c2p(a, b), radius=0.085, color=GRIS) for a, b in zip(df.tv, df.ventas)])
    s.play(Create(g), run_time=0.8)
    s.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.006), run_time=1.6)
    s.cue()
    q = rot("¿Por qué se abre?", ax.c2p(75, 26), NEGRO)
    s.play(FadeIn(q))
    s.cue()
    x, y0, y1 = 3.75, -2.95, 1.95
    ry = lambda r: y0 + (r / 50) * (y1 - y0)
    marcas = VGroup(*[Line([x - 0.4, ry(r), 0], [x + 0.4, ry(r), 0], stroke_width=2.5, color=grad(r)) for r in RS])
    rtit = VGroup(T("Radio (miles de USD)", 24, GRIS).move_to([x + 0.75, y1 + 0.4, 0]), T("0", 22, GRIS).move_to([x - 0.7, y0, 0]), T("50", 22, GRIS).move_to([x - 0.75, y1, 0]))
    s.play(FadeOut(q), pintar(dots, [GRIS] * len(dots), [grad(r) for r in RS]), FadeIn(marcas), FadeIn(rtit))
    s.cue()
    a, c = ValueTracker(12.0), ValueTracker(35.0)
    corte = lambda tr, col: always_redraw(lambda: VGroup(Line([x - 0.6, ry(tr.get_value()), 0], [x + 0.6, ry(tr.get_value()), 0], color=col, stroke_width=6), T(f"{tr.get_value():.0f}", 28, col, BOLD).move_to([x - 0.95, ry(tr.get_value()), 0])))
    ca, cc = corte(a, NEGRO), corte(c, ROJO)
    s.play(FadeIn(ca), FadeIn(cc))
    s.cue()
    cnt = always_redraw(lambda: VGroup(T(f"{int((RS >= c.get_value()).sum())} rojos", 28, ROJO, BOLD).move_to([5.75, ry(45), 0]), T(f"{int(((RS > a.get_value()) & (RS < c.get_value())).sum())} grises", 28, GRIS, BOLD).move_to([5.75, ry(25), 0]), T(f"{int((RS <= a.get_value()).sum())} negros", 28, NEGRO, BOLD).move_to([5.75, ry(5), 0])))
    ini = [grad(r) for r in RS]
    medio = [ManimColor(ROJO) if r >= 35 else ManimColor(NEGRO) if r <= 12 else grad(r) for r in RS]
    s.play(pintar(VGroup(*dots), ini, medio), pintar(VGroup(*marcas), ini, medio), FadeIn(cnt))
    s.cue()
    fin = [col_corte(r, 12, 35) for r in RS]
    s.play(pintar(VGroup(*dots), medio, fin), pintar(VGroup(*marcas), medio, fin))
    s.cue()
    t = etiqueta("Dos cortes puestos a mano", NEGRO, BLANCO, 26).move_to(ax.c2p(82, 28))
    s.play(FadeIn(t, shift=UP * 0.2), Indicate(ca, color=NEGRO), Indicate(cc, color=ROJO))
    s.cue()

    def act(_):
        va, vc = a.get_value(), c.get_value()
        for d, m_, r in zip(dots, marcas, RS):
            col = col_corte(r, va, vc)
            d.set_color(col); m_.set_color(col)

    dots.add_updater(act)
    s.play(a.animate.set_value(10), c.animate.set_value(40), run_time=1.5)
    s.play(a.animate.set_value(20), c.animate.set_value(25), run_time=1.8)
    s.play(a.animate.set_value(12), c.animate.set_value(35), run_time=1.3)
    s.cue()
    dots.remove_updater(act)
    g_ = RI["grupos"]
    t2 = rot(f"TV promedio: {g_['alto']['tv']:.0f} mil en rojos y {g_['bajo']['tv']:.0f} mil en negros", ax.c2p(158, 2.6), NEGRO)
    s.play(FadeOut(t), FadeIn(t2))
    s.cue()


def lineas(s):
    g, ax = ejes((0, 300), (0, 30), 11.8, 4.25, "TV (miles de USD)", "Ventas (miles)", (0, 100, 200, 300), (0, 10, 20, 30))
    g.move_to([0.1, -1.1, 0])
    dots = VGroup(*[Dot(ax.c2p(a, b), radius=0.075, color=col_corte(r, 12, 35)) for a, b, r in zip(df.tv, df.ventas, RS)])
    n0 = rot("200 mercados · la radio entra como número", ax.c2p(205, 3.2), NEGRO)
    s.play(Create(g), FadeIn(dots), FadeIn(n0), run_time=1)
    s.cue()
    eq = T(f"ventas = {coma(M['Intercept'])} + {coma(M['tv'], 4)}·tv + {coma(M['radio'], 4)}·radio + {coma(M['tv:radio'], 5)}·tv·radio", 30).move_to([0, 2.72, 0])
    s.play(FadeOut(n0), Write(eq), run_time=1.3)
    s.cue()
    sub = None
    G = RI["grupos"]
    def linea(k, col):
        nonlocal sub
        r = G[k]["radio"]
        nuevo = T(f"con radio = {coma(r, 1)}:   ventas = {coma(f_inter(0, r))} + {coma(G[k]['pend_modelo'], 4)}·tv", 30, col, BOLD).move_to([0, 2.05, 0])
        l = Line(ax.c2p(0, f_inter(0, r)), ax.c2p(300, f_inter(300, r)), color=col, stroke_width=7)
        s.play(*([FadeOut(sub)] if sub else []), FadeIn(nuevo, shift=DOWN * 0.15), run_time=0.5)
        sub = nuevo
        s.play(Create(l), run_time=1.3)
        s.cue()
    linea("alto", ROJO)
    linea("bajo", NEGRO)
    linea("medio", GRIS)
    H = [("", "recta aparte", "modelo"), ("Rojos", coma(G["alto"]["pend_sep"], 4), coma(G["alto"]["pend_modelo"], 4)), ("Negros", coma(G["bajo"]["pend_sep"], 4), coma(G["bajo"]["pend_modelo"], 4))]
    caja_ = Rectangle(width=5.6, height=1.5).set_stroke(CLARO, 2).set_fill(WHITE, 0.94).move_to([3.6, -2.2, 0])
    filas = VGroup()
    for i, (a, b, c) in enumerate(H):
        y = -1.72 - i * 0.48
        filas.add(T(a, 26, NEGRO, BOLD).move_to([1.2, y, 0], aligned_edge=LEFT), T(b, 26, GRIS if i == 0 else NEGRO).move_to([3.3, y, 0]), T(c, 26, GRIS if i == 0 else ROJO, BOLD).move_to([5.2, y, 0]))
    s.play(FadeIn(caja_), FadeIn(filas))
    s.cue()
    s.play(FadeIn(rot("Aquí: solo interacción, sin tv²", ax.c2p(70, 27), NEGRO)))
    s.cue()


def factor(s):
    e1 = T("ventas = b₀ + b₁·tv + b₂·radio + b₃·tv·radio", 44).move_to([0, 1.3, 0])
    s.play(Write(e1), run_time=1.4)
    s.cue()
    e2 = Text("ventas = b₀ + b₁·tv + b₂·radio + b₃·tv·radio", font=E.CUERPO, font_size=44, color=NEGRO, t2c={"b₁·tv": ROJO, "b₃·tv·radio": ROJO}).move_to([0, 1.3, 0])
    s.play(FadeOut(e1), FadeIn(e2), run_time=0.6)
    e3 = Text("ventas = (b₀ + b₂·radio) + (b₁ + b₃·radio)·tv", font=E.CUERPO, font_size=44, color=NEGRO, t2c={"(b₁ + b₃·radio)": ROJO}).move_to([0, 0.05, 0])
    s.play(TransformFromCopy(e2, e3), run_time=1.5)
    s.cue()
    caja_ = SurroundingRectangle(e3[-16:-3], color=ROJO, buff=0.1)
    et = etiqueta("la pendiente de la TV", ROJO, BLANCO, 28).move_to([2.4, -1.1, 0])
    num = T(f"pendiente = {coma(M['tv'], 4)} + {coma(M['tv:radio'], 5)} · radio", 42, NEGRO, BOLD).move_to([0, -2.15, 0])
    s.play(FadeIn(et, shift=UP * 0.2), FadeIn(num, shift=UP * 0.2))
    s.cue()
    t = cabe(Z("UNA VARIABLE CAMBIA LA PENDIENTE DE LA OTRA", 36, ROJO), 13.2).move_to([0, -3.2, 0])
    s.play(FadeIn(t, shift=UP * 0.2))
    s.cue()


def pendiente(s):
    g, ax = ejes((0, 300), (0, 32), 8.3, 4.9, "TV (miles de USD)", "Ventas (miles)", (0, 100, 200, 300), (0, 10, 20, 30))
    g.move_to([-2.65, -0.55, 0])
    fondo = VGroup(*[Dot(ax.c2p(a, b), radius=0.06, color="#E3E3E3") for a, b in zip(df.tv, df.ventas)])
    r, modo = ValueTracker(0.0), ValueTracker(0.0)
    pend = lambda: (PL["tv"] if modo.get_value() > 0.5 else M["tv"] + M["tv:radio"] * r.get_value())
    orig = lambda: (PL["Intercept"] + PL["radio"] * r.get_value() if modo.get_value() > 0.5 else M["Intercept"] + M["radio"] * r.get_value())
    lin = always_redraw(lambda: Line(ax.c2p(0, orig()), ax.c2p(300, orig() + 300 * pend()), color=NEGRO if modo.get_value() > 0.5 else ROJO, stroke_width=8))
    panel = always_redraw(lambda: VGroup(T("Radio del mercado", 26, GRIS), Z(f"{r.get_value():.0f} mil", 54), T("Cada mil USD en TV traen", 26, GRIS), Z(f"{pend() * 1000:.0f}", 90, NEGRO if modo.get_value() > 0.5 else ROJO), T("unidades", 28, GRIS)).arrange(DOWN, buff=0.14).move_to([4.75, -0.35, 0]))
    s.play(Create(g), FadeIn(fondo), Create(lin), FadeIn(panel), run_time=1)
    s.cue()
    s.play(r.animate.set_value(20), run_time=2.2, rate_func=smooth)
    s.cue()
    s.play(r.animate.set_value(45), run_time=2.2, rate_func=smooth)
    s.cue()
    tag = etiqueta("Sin interacción", NEGRO, BLANCO, 28).move_to(ax.c2p(70, 29))
    modo.set_value(1)
    s.play(FadeIn(tag), run_time=0.3)
    s.play(r.animate.set_value(0), run_time=1.8, rate_func=smooth)
    s.play(r.animate.set_value(45), run_time=1.8, rate_func=smooth)
    s.cue()


def superficie(s):
    s.set_camera_orientation(phi=66 * DEGREES, theta=-118 * DEGREES, zoom=0.86)
    ax = ThreeDAxes(x_range=[0, 300, 100], y_range=[0, 50, 25], z_range=[0, 32, 10], x_length=7.4, y_length=5.2, z_length=3.8, tips=False, axis_config={"color": NEGRO, "include_ticks": False, "include_tip": False}).shift(IN * 0.55 + LEFT * 0.2)
    for tx, p in (("TV", (330, 0, 0)), ("Radio", (0, 57, 0)), ("Ventas", (0, 0, 35))):
        l = T(tx, 28, GRIS, BOLD).move_to(ax.c2p(*p))
        s.add_fixed_orientation_mobjects(l)
    def sup(f):
        return Surface(lambda u, v: ax.c2p(u, v, f(u, v)), u_range=[0, 300], v_range=[0, 50], resolution=(16, 10), checkerboard_colors=["#F5A9AC", "#F08A8E"], fill_opacity=0.78, stroke_color=WHITE, stroke_width=0.6)
    def corte(f, r, c):
        return ParametricFunction(lambda t: ax.c2p(t, r, f(t, r)), t_range=[0, 300, 6], color=c, stroke_width=9)
    h = sup(f_plano)
    s.play(Create(ax), run_time=0.8)
    s.play(FadeIn(h), run_time=1)
    s.cue()
    a0, b0 = corte(f_plano, 6, NEGRO), corte(f_plano, 42, "#8A0F14")
    s.play(Create(a0), Create(b0), run_time=1.4)
    s.begin_ambient_camera_rotation(rate=0.07)
    s.cue()
    s.play(Transform(h, sup(f_inter)), Transform(a0, corte(f_inter, 6, NEGRO)), Transform(b0, corte(f_inter, 42, "#8A0F14")), run_time=3.2, rate_func=smooth)
    s.cue()
    s.play(Indicate(b0, color="#8A0F14", scale_factor=1.0), run_time=1)
    s.cue()
    s.cue()
    s.stop_ambient_camera_rotation()


def serie_lineas(s, ax, xs, ys, col, ancho=7):
    return VMobject(stroke_color=col, stroke_width=ancho).set_points_as_corners([ax.c2p(a, b) for a, b in zip(xs, ys)])


def ejco2(s):
    c = RI["co2"]
    g, ax = ejes((3, 27), (0, 530), 11.8, 4.9, "Consumo (litros por 100 km)", "CO₂ (gramos por km)", (5, 10, 15, 20, 25), (0, 250, 500))
    g.move_to([-0.4, -0.55, 0])
    col = {"X": GRIS, "Z": GRIS, "D": NEGRO, "E": ROJO}
    pts = VGroup(*[Dot(ax.c2p(a, b), radius=0.07, color=col[t]).set_opacity(0.75) for a, b, t in c["puntos"] if t in col])
    s.play(Create(g), run_time=0.7)
    s.play(LaggedStart(*[GrowFromCenter(d) for d in pts], lag_ratio=0.006), run_time=1.5)
    s.cue()
    def linea(t, color, nombre, dx):
        q = c["grupos"][t]
        l = Line(ax.c2p(q["lo"], q["a"] + q["b"] * q["lo"]), ax.c2p(q["hi"], q["a"] + q["b"] * q["hi"]), color=color, stroke_width=8)
        e_ = rot(f"{nombre}: {q['b']:.0f}", ax.c2p(q["hi"] + dx, q["a"] + q["b"] * q["hi"] + 22), color)
        return Create(l), FadeIn(e_)
    s.play(*linea("X", GRIS, "Gasolina", -2.8), run_time=1.2)
    s.cue()
    s.play(*linea("D", NEGRO, "Diésel", -1.2), run_time=0.9)
    s.play(*linea("E", ROJO, "Etanol", -2.5), run_time=0.9)
    s.cue()
    s.play(FadeIn(rot("La pendiente depende del combustible", ax.c2p(19, 90), NEGRO)))
    s.cue()


def ejsuper(s):
    q = RI["super"]["cat"]
    pct = lambda v: f"{v * 100:.0f} %".replace("-", "−")
    g, ax = ejes((0, 0.8), (-1.9, 0.6), 11.6, 4.9, "Descuento", "Margen sobre la venta", (0, 0.2, 0.4, 0.6, 0.8), (-1.5, -1, -0.5, 0, 0.5), fmt=pct)
    g.move_to([-0.3, -0.55, 0])
    cero = DashedLine(ax.c2p(0, 0), ax.c2p(0.8, 0), color=CLARO)
    col = {"Muebles": GRIS, "Suministros de Oficina": ROJO, "Tecnología": NEGRO}
    pts = VGroup(*[Dot(ax.c2p(float(x), y), radius=0.11, color=col[c]) for c, v in q.items() for x, y in v["medias"].items() if -1.9 <= y <= 0.6])
    ley = VGroup(*[T(n, 24, c_, BOLD) for n, c_ in (("Suministros de oficina", ROJO), ("Muebles", GRIS), ("Tecnología", NEGRO))]).arrange(RIGHT, buff=0.4).move_to([2.9, 2.42, 0])
    s.play(Create(g), Create(cero), run_time=0.8)
    s.play(LaggedStart(*[GrowFromCenter(d) for d in pts], lag_ratio=0.05), FadeIn(ley), run_time=1.3)
    s.cue()
    ls = []
    for c in ("Suministros de Oficina", "Muebles", "Tecnología"):
        v = q[c]
        xs = np.linspace(0, 0.8, 80)
        ls.append(curva(ax, xs, v["a"] + v["b"] * xs, -1.9, 0.6, col[c], 7))
    txt = VGroup(rot("−21 puntos por cada 10 de descuento", ax.c2p(0.26, -1.05), ROJO), rot("−17", ax.c2p(0.73, -1.28), GRIS), rot("−12", ax.c2p(0.74, -0.45), NEGRO))
    s.play(*[Create(l) for l in ls], FadeIn(txt), run_time=1.5)
    s.cue()
    a1, b1, a2, b2 = q["Suministros de Oficina"]["a"], q["Suministros de Oficina"]["b"], q["Tecnología"]["a"], q["Tecnología"]["b"]
    xc = (a2 - a1) / (b1 - b2)
    s.play(Create(Circle(radius=0.32, color=NEGRO, stroke_width=4).move_to(ax.c2p(xc, a1 + b1 * xc))), FadeIn(rot("Las líneas se cruzan", ax.c2p(0.34, 0.42), NEGRO)))
    s.cue()


def ejtitanic(s):
    t = RI["titanic"]["tabla"]
    g, ax = ejes((0.6, 3.4), (0, 100), 9.6, 4.9, "Clase del pasaje", "Sobrevivieron (%)", (), (0, 50, 100))
    g.move_to([-1.0, -0.55, 0])
    for i, n in zip((1, 2, 3), ("Primera", "Segunda", "Tercera")):
        g.add(T(n, 26, GRIS).next_to(ax.c2p(i, 0), DOWN, buff=0.14))
    def serie(k, c):
        ys = [t[k][str(i)] * 100 for i in (1, 2, 3)]
        return VGroup(serie_lineas(s, ax, (1, 2, 3), ys, c), *[Dot(ax.c2p(i, y), radius=0.14, color=c) for i, y in zip((1, 2, 3), ys)])
    m_, h_ = serie("female", ROJO), serie("male", NEGRO)
    s.play(Create(g), run_time=0.6)
    s.play(Create(m_), Create(h_), FadeIn(T("Mujeres", 30, ROJO, BOLD).move_to(ax.c2p(3.35, 62))), FadeIn(T("Hombres", 30, NEGRO, BOLD).move_to(ax.c2p(3.35, 22))), run_time=1.4)
    s.cue()
    an = []
    for i in (1, 2, 3):
        a, b = t["female"][str(i)] * 100, t["male"][str(i)] * 100
        an += [DoubleArrow(ax.c2p(i, b), ax.c2p(i, a), color=AZUL, stroke_width=5, buff=0.16, tip_length=0.22), rot(f"{a - b:.0f} puntos", ax.c2p(i + 0.32, (a + b) / 2), AZUL)]
    s.play(LaggedStart(*[FadeIn(x) for x in an], lag_ratio=0.25), run_time=2.4)
    s.cue()
    s.play(Indicate(VGroup(*an), color=ROJO, scale_factor=1.03), run_time=1.1)
    s.cue()


def ejprensa(s):
    q = RI["radio_prensa"]
    p = q["params"]
    f = lambda r, pr: p["Intercept"] + p["tv"] * q["tv"] + p["radio"] * r + p["prensa"] * pr + p["radio:prensa"] * r * pr
    g, ax = ejes((0, 50), (8, 21), 11.0, 4.9, "Radio (miles de USD)", "Ventas pronosticadas (miles)", (0, 25, 50), (10, 15, 20))
    g.move_to([-0.4, -0.55, 0])
    lo, hi = q["prensa_q"]
    s.play(Create(g), run_time=0.7)
    a, b = Line(ax.c2p(0, f(0, lo)), ax.c2p(50, f(50, lo)), color=NEGRO, stroke_width=8), Line(ax.c2p(0, f(0, hi)), ax.c2p(50, f(50, hi)), color=ROJO, stroke_width=8)
    s.play(Create(a), Create(b), FadeIn(rot("Mucha prensa", ax.c2p(41, f(50, hi) + 1.6), ROJO)), FadeIn(rot("Poca prensa", ax.c2p(42, f(42, lo) - 1.8), NEGRO)), run_time=1.4)
    s.cue()
    s.play(FadeIn(etiqueta("valor p de radio × prensa: 0,50", NEGRO, BLANCO, 30).move_to(ax.c2p(19, 19.4))))
    s.cue()
    s.play(FadeIn(Z("HAY QUE PROBARLO", 44, ROJO).move_to(ax.c2p(33, 10))))
    s.cue()


def python(s):
    sn = RI["snips"][TOMA["snip"]]
    lineas_ = sn["codigo"].split("\n")
    con_imagen = TOMA.get("imagen", False)
    ancho = 7.7 if con_imagen else 12.7
    font = min(26, ancho / (max(map(len, lineas_)) * 0.0092))
    cw = Text("M" * 20, font="Menlo", font_size=font).width / 20
    if con_imagen:
        tarjeta = Rectangle(width=8.2, height=5.75).set_stroke(width=0).set_fill("#141414", 1).move_to([-2.5, -0.35, 0])
        x0, y_top = -6.4, 2.05
    else:
        tarjeta = Rectangle(width=13.4, height=3.25).set_stroke(width=0).set_fill("#141414", 1).move_to([0, 1.05, 0])
        x0, y_top = -6.4, 2.25
    paso = font * 0.0215
    objetos = []
    for i, l in enumerate(lineas_):
        sang = len(l) - len(l.lstrip())
        o = Text(l.strip(), font="Menlo", font_size=font, color=BLANCO).move_to([x0 + sang * cw, y_top - i * paso, 0], aligned_edge=LEFT)
        objetos.append(o)
    s.play(FadeIn(tarjeta), run_time=0.4)
    hechas, salida_en = 0, TOMA.get("salida_en", len(TOMA["beats"]) - 1)
    for k, hasta in enumerate(TOMA["revela"]):
        for o in objetos[hechas:hasta]:
            s.play(AddTextLetterByLetter(o, time_per_char=0.016), run_time=max(0.35, len(o.text) * 0.016))
        hechas = max(hechas, hasta)
        if k == salida_en:
            if con_imagen:
                im = ImageMobject(str(AQUI / "datos" / "salida_p5.png"))
                im.width = 5.2
                im.move_to([4.25, -0.4, 0])
                s.play(FadeIn(im, shift=LEFT * 0.3))
            elif sn["salida"]:
                fondo = Rectangle(width=13.4, height=2.55).set_stroke(width=0).set_fill("#EFEFEF", 1).move_to([0, -2.1, 0])
                et = T("Salida", 22, GRIS, BOLD).move_to([-6.4, -1.05, 0], aligned_edge=LEFT)
                txt = Text(sn["salida"], font="Menlo", font_size=25, color=NEGRO, line_spacing=0.8)
                if txt.height > 1.75:
                    txt.scale_to_fit_height(1.75)
                if txt.width > 12.6:
                    txt.scale_to_fit_width(12.6)
                txt.move_to([-6.4, -2.3, 0], aligned_edge=LEFT)
                s.play(FadeIn(fondo), FadeIn(et), FadeIn(txt, shift=UP * 0.1), run_time=0.6)
        s.cue()


def trampas(s):
    actual = None
    for i, (a, b) in enumerate(TOMA["cartas"]):
        g = VGroup(etiqueta(f"ERROR {i + 1}", ROJO, BLANCO, 24), cabe(Z(a, 110, NEGRO), 12.6), Tw(b, 42, NEGRO, 12.0)).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to([-6.3, -0.2, 0], aligned_edge=LEFT)
        if actual is not None:
            s.play(FadeOut(actual, shift=UP * 0.3), FadeIn(g, shift=UP * 0.3), run_time=0.5)
        else:
            s.play(FadeIn(g, shift=UP * 0.3), run_time=0.5)
        actual = g
        s.cue()


def traintest(s):
    tr_i, te_i = train_test_split(np.arange(200), test_size=0.25, random_state=42)
    malla = [np.array([-5.7 + i * 0.6, 1.75 - j * 0.4, 0]) for j in range(10) for i in range(20)]
    dots = VGroup(*[Dot(p, radius=0.12, color=GRIS) for p in malla])
    et = T("200 mercados", 28, GRIS, BOLD).move_to([-6.5, 2.4, 0], aligned_edge=LEFT)
    s.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.006), FadeIn(et), run_time=1.5)
    s.cue()
    ex = etiqueta("Estudiar con el examen en la mano", NEGRO, BLANCO, 32).move_to([0, -2.75, 0])
    s.play(FadeIn(ex, shift=UP * 0.2))
    s.cue()
    rng = np.random.default_rng(42)
    s.play(FadeOut(ex), *[d.animate.move_to(malla[i]) for d, i in zip(dots, rng.permutation(200))], run_time=1.3, rate_func=smooth)
    s.play(*[d.animate.move_to(malla[i]) for d, i in zip(dots, rng.permutation(200))], run_time=1.1, rate_func=smooth)
    s.cue()
    izq = [np.array([-6.35 + c * 0.34, 1.75 - f * 0.4, 0]) for f in range(10) for c in range(15)]
    der = [np.array([3.55 + c * 0.55, 1.75 - f * 0.4, 0]) for f in range(10) for c in range(5)]
    e_tr = T("Entrenamiento: 150", 30, NEGRO, BOLD).move_to([-6.5, 2.4, 0], aligned_edge=LEFT)
    s.play(FadeOut(et), FadeIn(e_tr), *[dots[int(i)].animate.move_to(izq[k]) for k, i in enumerate(tr_i)], *[dots[int(i)].animate.set_opacity(0.35) for i in te_i], run_time=1.5)
    s.cue()
    caja_ = Rectangle(width=3.3, height=4.15).set_stroke(ROJO, 5).move_to([4.65, -0.05, 0])
    e_te = T("Prueba: 50", 30, ROJO, BOLD).move_to([3.0, 2.4, 0], aligned_edge=LEFT)
    cuerpo = Rectangle(width=0.62, height=0.48).set_stroke(width=0).set_fill(ROJO, 1).move_to([6.1, 2.42, 0])
    arco = Arc(radius=0.2, start_angle=0, angle=PI, color=ROJO, stroke_width=7).move_to([6.1, 2.8, 0])
    s.play(*[dots[int(i)].animate.move_to(der[k]).set_color(ROJO).set_opacity(1) for k, i in enumerate(te_i)], Create(caja_), FadeIn(e_te), FadeIn(cuerpo), Create(arco), run_time=1.5)
    s.cue()
    mod = VGroup(Rectangle(width=2.2, height=1.3).set_stroke(width=0).set_fill(NEGRO, 1), Z("MODELO", 24, BLANCO)).move_to([0.8, 0, 0])
    fl = Arrow([-1.55, 0, 0], [-0.32, 0, 0], color=NEGRO, stroke_width=8, buff=0, max_tip_length_to_length_ratio=0.35)
    s.play(FadeIn(mod, scale=0.8), GrowArrow(fl), run_time=0.9)
    s.cue()
    fl2 = Arrow([1.92, 0, 0], [2.95, 0, 0], color=ROJO, stroke_width=8, buff=0, max_tip_length_to_length_ratio=0.35)
    u = T("Una sola vez", 24, ROJO, BOLD).move_to([1.55, -0.95, 0])
    s.play(arco.animate.shift(UP * 0.16 + RIGHT * 0.2).rotate(0.5), GrowArrow(fl2), FadeIn(u), run_time=1)
    s.cue()
    def fila(y, nom, v, col):
        tx = T(nom, 28).move_to([-6.4, y, 0], aligned_edge=LEFT)
        b = Rectangle(width=v * 2.6, height=0.34).set_stroke(width=0).set_fill(col, 1).move_to([-3.6, y, 0], aligned_edge=LEFT)
        return tx, b, Z(coma(v), 32, col).next_to(b, RIGHT, buff=0.18)
    e = R["escalera"]["plano"]
    a = fila(-2.65, "Entrenamiento", e["mae_tr"], GRIS)
    b = fila(-3.25, "Prueba", e["mae_te"], ROJO)
    s.play(FadeIn(a[0]), GrowFromEdge(a[1], LEFT), FadeIn(a[2]), FadeIn(b[0]), GrowFromEdge(b[1], LEFT), FadeIn(b[2]), run_time=1.1)
    s.cue()
    m_ = Z("TRAIN Y TEST", 38, NEGRO).move_to([4.4, -2.68, 0])
    s.play(FadeIn(m_, shift=UP * 0.2))
    s.cue()
    az = Text("random_state = 42", font="Menlo", font_size=30, color=BLANCO)
    fondo_ = Rectangle(width=az.width + 0.5, height=az.height + 0.35).set_stroke(width=0).set_fill("#141414", 1).move_to([4.4, -3.35, 0])
    az.move_to(fondo_)
    s.play(FadeIn(fondo_), AddTextLetterByLetter(az, time_per_char=0.03))
    s.cue()


CONSTRUIR = {k: v for k, v in globals().items() if k in ("portada", "ilus", "apuesta", "mapa", "antesdespues", "escalera", "radiotv", "promesacorr", "grados", "mercado", "freno", "escala", "rejilla", "final", "raiz", "co2", "guia", "ejercicio", "cierre", "separar", "lineas", "factor", "pendiente", "superficie", "ejco2", "ejsuper", "ejtitanic", "ejprensa", "python", "trampas", "traintest")}

if TOMA["tipo"] == "superficie":
    Toma = type("Toma", (ConVoz, ThreeDScene), {"construct": lambda self: superficie(self)})
elif TOMA["tipo"] == "clip":
    Toma = type("Toma", (ConVoz, getattr(E, TOMA["base"])), {})
else:
    Toma = type("Toma", (ConVoz, E.Escena), {"construct": lambda self: CONSTRUIR[TOMA["tipo"]](self)})
