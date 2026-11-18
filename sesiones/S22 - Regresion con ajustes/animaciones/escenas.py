# -*- coding: utf-8 -*-
"""Ocho animaciones de la clase de regresión con ajustes, hechas con Manim Community sobre los datos reales de Bebidas Cumbre.

Render: manim -r 1920,1080 --fps 30 escenas.py S1Ajuste   (o bash render.sh para todas)
La banda superior del cuadro (y > 2.6) queda en blanco: ahí el deck pone el título de la slide.
"""
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from manim import *
from sklearn.linear_model import Lasso, LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

warnings.filterwarnings("ignore")
config.background_color = "#FFFFFF"
ROJO, NEGRO, GRIS, CLARO, AZUL, AMBAR = "#E11B22", "#111111", "#7A7A7A", "#DADADA", "#1F6FB2", "#F2A900"
CUERPO, TITULO = "Helvetica Neue", "Zalando Sans Expanded"
df = pd.read_csv(Path(__file__).resolve().parents[1] / "d2l" / "mercados-bebidas-cumbre.csv")


class Escena(Scene):
    """cue() marca el fin de una frase narrada. Sin voz no hace nada."""

    def cue(self):
        pass


def T(s, size=30, color=NEGRO, weight=NORMAL):
    return Text(s, font=CUERPO, font_size=size, color=color, weight=weight)


def Z(s, size=40, color=NEGRO):
    return Text(s, font=TITULO, font_size=size, color=color, weight=HEAVY)


def ejes(xr, yr, w, h, xlab, ylab, xt=(), yt=(), fmt=str, marco=True):
    ax = Axes(x_range=[xr[0], xr[1], (xr[1] - xr[0])], y_range=[yr[0], yr[1], (yr[1] - yr[0])], x_length=w, y_length=h, tips=False,
              axis_config={"color": NEGRO, "stroke_width": 2, "include_ticks": False})
    g = VGroup()
    if marco:
        ax.x_axis.set_opacity(0)
        ax.y_axis.set_opacity(0)
        g.add(Line(ax.c2p(xr[0], yr[0]), ax.c2p(xr[1], yr[0]), color=NEGRO, stroke_width=2), Line(ax.c2p(xr[0], yr[0]), ax.c2p(xr[0], yr[1]), color=NEGRO, stroke_width=2))
    for v in xt:
        g.add(T(fmt(v), 22, GRIS).next_to(ax.c2p(v, yr[0]), DOWN, buff=0.14))
    for v in yt:
        g.add(T(fmt(v), 22, GRIS).next_to(ax.c2p(xr[0], v), LEFT, buff=0.14))
    resto = VGroup()
    if xlab:
        resto.add(T(xlab, 24, GRIS).next_to(ax.c2p((xr[0] + xr[1]) / 2, yr[0]), DOWN, buff=0.5))
    if ylab:
        resto.add(T(ylab, 24, GRIS).next_to(ax.c2p(xr[0], yr[1]), UP, buff=0.14, aligned_edge=LEFT))
    return VGroup(ax, g, *resto), ax


def curva(ax, xs, ys, ymin, ymax, color=ROJO, ancho=5):
    """Curva recortada al área de los ejes: lo que se sale del gráfico no se dibuja."""
    g = VGroup()
    tramo = []
    for a, b in zip(xs, ys):
        if ymin <= b <= ymax:
            tramo.append(ax.c2p(a, b))
        else:
            if len(tramo) > 1:
                g.add(VMobject(stroke_color=color, stroke_width=ancho).set_points_as_corners(tramo))
            tramo = []
    if len(tramo) > 1:
        g.add(VMobject(stroke_color=color, stroke_width=ancho).set_points_as_corners(tramo))
    return g


class S1Ajuste(Escena):
    """Ajustar es mover la recta hasta que la suma de cuadrados sea mínima."""

    def construct(self):
        d = df.sample(22, random_state=11)
        x, y = d.tv.values, d.ventas.values
        xb, yb = x.mean(), y.mean()
        bols = np.sum((x - xb) * (y - yb)) / np.sum((x - xb) ** 2)
        sse = lambda b: float(np.sum((y - (yb + b * (x - xb))) ** 2))
        grupo, ax = ejes((0, 300), (0, 30), 7.4, 5.0, "TV (miles de USD)", "Ventas (miles)", (0, 100, 200, 300), (0, 10, 20, 30))
        grupo.move_to([-2.85, -0.45, 0])
        puntos = VGroup(*[Dot(ax.c2p(a, b), radius=0.075, color=NEGRO) for a, b in zip(x, y)])
        pend = ValueTracker(0.0)
        recta = always_redraw(lambda: Line(ax.c2p(0, yb + pend.get_value() * (0 - xb)), ax.c2p(300, yb + pend.get_value() * (300 - xb)), color=ROJO, stroke_width=5))

        def cuadrados():
            g = VGroup()
            for a, c in zip(x, y):
                h = yb + pend.get_value() * (a - xb)
                p0, p1 = ax.c2p(a, c), ax.c2p(a, h)
                s = abs(p1[1] - p0[1])
                if s < 0.02:
                    continue
                signo = 1 if a < xb else -1
                g.add(Square(side_length=s).set_stroke(ROJO, 1, 0.8).set_fill(ROJO, 0.13).move_to([p0[0] + signo * s / 2, (p0[1] + p1[1]) / 2, 0]))
            return g

        cuad = always_redraw(cuadrados)
        rango = (-0.04, 0.13)
        g2, ax2 = ejes(rango, (0, sse(rango[1]) * 1.05), 3.9, 3.2, "pendiente de la recta", "", (0,), ())
        g2.move_to([4.55, -0.75, 0])
        par = ax2.plot(sse, x_range=[rango[0], rango[1], 0.001], color=CLARO, stroke_width=5)
        bola = always_redraw(lambda: Dot(ax2.c2p(pend.get_value(), sse(pend.get_value())), radius=0.12, color=ROJO))
        cont = always_redraw(lambda: VGroup(T("Suma de cuadrados", 26, GRIS), Z(f"{sse(pend.get_value()):,.0f}".replace(",", "."), 46, ROJO)).arrange(DOWN, buff=0.1).move_to([4.55, 1.75, 0]))

        self.play(Create(grupo), run_time=1)
        self.play(LaggedStart(*[GrowFromCenter(p) for p in puntos], lag_ratio=0.04), run_time=1.4)
        self.wait(0.3)
        nota = T("Línea base: el promedio para todos", 28, NEGRO).move_to([-2.65, 2.3, 0], aligned_edge=LEFT)
        self.play(Create(recta), FadeIn(nota), run_time=1)
        self.cue()
        self.wait(0.6)
        self.play(FadeIn(cuad), FadeIn(g2), Create(par), FadeIn(bola), FadeIn(cont), run_time=1.2)
        self.cue()
        self.wait(0.6)
        self.play(FadeOut(nota))
        n2 = T("Cada error se eleva al cuadrado", 28).move_to([-2.65, 2.3, 0], aligned_edge=LEFT)
        self.play(FadeIn(n2))
        self.play(pend.animate.set_value(0.115), run_time=2.6, rate_func=smooth)
        self.cue()
        self.wait(0.3)
        self.play(pend.animate.set_value(-0.025), run_time=3, rate_func=smooth)
        self.cue()
        self.wait(0.3)
        self.play(FadeOut(n2))
        n3 = T("Ajustar es bajar hasta el fondo", 28).move_to([-2.65, 2.3, 0], aligned_edge=LEFT)
        self.play(FadeIn(n3))
        self.play(pend.animate.set_value(bols), run_time=3.4, rate_func=smooth)
        anillo = Circle(radius=0.3, color=ROJO, stroke_width=4).move_to(ax2.c2p(bols, sse(bols)))
        fin = T("Mínimo. Aquí se detiene.", 26, ROJO, BOLD).next_to(anillo, UP, buff=0.3).set_x(4.4)
        self.play(Create(anillo), FadeIn(fin))
        self.cue()
        self.wait(2.5)
        self.cue()


class S2Columnas(Escena):
    """Un polinomio sigue siendo regresión lineal: solo son columnas nuevas."""

    def construct(self):
        d = df.iloc[[0, 1, 2, 3, 4]]
        cab = ["tv", "radio", "tv × radio", "tv²"]
        val = [[f"{a:.1f}".replace(".", ",") for a in d.tv], [f"{a:.1f}".replace(".", ",") for a in d.radio],
               [f"{a * b:,.0f}".replace(",", ".") for a, b in zip(d.tv, d.radio)], [f"{a ** 2:,.0f}".replace(",", ".") for a in d.tv]]
        xs = [-4.1, -1.7, 1.1, 4.2]
        col = []
        for j, c in enumerate(cab):
            color = NEGRO if j < 2 else ROJO
            g = VGroup(Z(c, 30, color).move_to([xs[j], 2.05, 0]))
            for i, v in enumerate(val[j]):
                g.add(T(v, 32, color).move_to([xs[j], 1.3 - i * 0.62, 0]))
            col.append(g)
        linea = Line([-5.3, 1.68, 0], [5.3, 1.68, 0], color=CLARO, stroke_width=3)
        ec1 = T("ventas  =  b₀  +  b₁·tv  +  b₂·radio", 40).move_to([0, -2.1, 0])
        self.play(FadeIn(col[0], shift=UP * 0.2), FadeIn(col[1], shift=UP * 0.2), Create(linea), run_time=1)
        self.play(Write(ec1), run_time=1.4)
        self.cue()
        self.wait(1.2)
        ec2 = T("ventas  =  b₀  +  b₁·tv  +  b₂·radio  +  b₃·(tv × radio)", 40).move_to([0, -2.1, 0])
        self.play(LaggedStart(*[FadeIn(m, scale=0.6) for m in col[2]], lag_ratio=0.15), run_time=1.8)
        self.play(FadeOut(ec1), FadeIn(ec2), run_time=0.8)
        self.cue()
        self.wait(1.2)
        ec3 = T("ventas  =  b₀  +  b₁·tv  +  b₂·radio  +  b₃·(tv × radio)  +  b₄·tv²", 34).move_to([0, -2.1, 0])
        self.play(LaggedStart(*[FadeIn(m, scale=0.6) for m in col[3]], lag_ratio=0.15), run_time=1.8)
        self.play(FadeOut(ec2), FadeIn(ec3), run_time=0.8)
        self.cue()
        self.wait(1.2)
        msg = Z("SIGUE SIENDO UNA SUMA DE COLUMNAS", 34, ROJO).move_to([0, -3.15, 0])
        self.play(FadeIn(msg, shift=UP * 0.2), Indicate(ec3, color=NEGRO, scale_factor=1.04), run_time=1.2)
        self.cue()
        self.wait(3)


class S3Abanico(Escena):
    """El plano da rectas paralelas. Con interacción y curvatura la TV rinde según la radio."""

    def construct(self):
        import statsmodels.formula.api as smf
        pl = smf.ols("ventas ~ tv + radio", df).fit().params
        cu = smf.ols("ventas ~ tv + radio + tv:radio + I(tv**2)", df).fit().params
        f0 = lambda t, r: pl["Intercept"] + pl["tv"] * t + pl["radio"] * r
        f1 = lambda t, r: cu["Intercept"] + cu["tv"] * t + cu["radio"] * r + cu["tv:radio"] * t * r + cu["I(tv ** 2)"] * t * t
        grupo, ax = ejes((0, 300), (0, 30), 10.6, 5.0, "TV (miles de USD)", "Ventas (miles)", (0, 100, 200, 300), (0, 10, 20, 30))
        grupo.move_to([-0.9, -0.45, 0])
        al = df[df.radio >= 35]
        ba = df[df.radio <= 12]
        pa = VGroup(*[Dot(ax.c2p(a, b), radius=0.075, color=ROJO) for a, b in zip(al.tv, al.ventas)])
        pb = VGroup(*[Dot(ax.c2p(a, b), radius=0.075, color=NEGRO) for a, b in zip(ba.tv, ba.ventas)])
        ra, rb = al.radio.mean(), ba.radio.mean()
        k = ValueTracker(0.0)
        xs = np.linspace(1, 296, 90)
        la = always_redraw(lambda: curva(ax, xs, (1 - k.get_value()) * f0(xs, ra) + k.get_value() * f1(xs, ra), 0, 30, ROJO, 6))
        lb = always_redraw(lambda: curva(ax, xs, (1 - k.get_value()) * f0(xs, rb) + k.get_value() * f1(xs, rb), 0, 30, NEGRO, 6))
        ea = T("Mucha radio", 28, ROJO, BOLD).move_to([5.75, 1.75, 0])
        eb = T("Poca radio", 28, NEGRO, BOLD).move_to([5.75, -0.55, 0])
        self.play(Create(grupo), run_time=1)
        self.play(LaggedStart(*[GrowFromCenter(p) for p in VGroup(*pa, *pb)], lag_ratio=0.015), run_time=1.5)
        self.play(FadeIn(ea), FadeIn(eb))
        self.cue()
        self.wait(0.4)
        self.play(Create(la), Create(lb), run_time=1.4)
        n1 = T("El plano obliga a dos rectas paralelas", 30).move_to([-2.9, 2.3, 0], aligned_edge=LEFT)
        self.play(FadeIn(n1))
        self.cue()
        self.wait(2.2)
        self.play(FadeOut(n1))
        n2 = T("Le dejamos doblarse", 30).move_to([-2.9, 2.3, 0], aligned_edge=LEFT)
        self.play(FadeIn(n2))
        self.play(k.animate.set_value(1), run_time=4, rate_func=smooth)
        self.cue()
        self.wait(0.5)
        self.play(FadeOut(n2))
        g0 = abs(f1(250, ra) - f1(250, rb))
        g1 = abs(f1(20, ra) - f1(20, rb))
        fa1 = DoubleArrow(ax.c2p(250, f1(250, rb)), ax.c2p(250, f1(250, ra)), color=AZUL, stroke_width=4, buff=0.05, tip_length=0.2)
        fa2 = DoubleArrow(ax.c2p(20, f1(20, rb)), ax.c2p(20, f1(20, ra)), color=AZUL, stroke_width=4, buff=0.05, tip_length=0.2)
        ta1 = T("Con mucha TV: +" + f"{g0:.1f}".replace(".", ",") + " mil", 26, AZUL, BOLD).move_to(ax.c2p(205, 6.2))
        ta2 = T("Con poca TV: +" + f"{g1:.1f}".replace(".", ",") + " mil", 26, AZUL, BOLD).move_to(ax.c2p(70, 19.5))
        self.play(GrowFromCenter(fa2), FadeIn(ta2))
        self.cue()
        self.wait(0.8)
        self.play(GrowFromCenter(fa1), FadeIn(ta1))
        n3 = T("La radio rinde según la TV que ya hay", 30, AZUL, BOLD).move_to([-2.9, 2.3, 0], aligned_edge=LEFT)
        self.play(FadeIn(n3))
        self.cue()
        self.wait(3)


def muestra(n_tr, seed, n_te=45):
    d = df.sample(frac=1, random_state=seed)
    return d.iloc[:n_tr], d.iloc[n_tr:n_tr + n_te]


class S4Grado(Escena):
    """Cada grado baja el error de entrenamiento. El de prueba se dispara."""

    def construct(self):
        tr, te = muestra(13, 3)
        xs = np.linspace(tr.tv.min(), tr.tv.max(), 260)
        grados = [1, 2, 3, 5, 7, 9, 12]
        F = {g: np.polynomial.Chebyshev.fit(tr.tv.values, tr.ventas.values, g, domain=[0, 300]) for g in grados}
        Ys = np.array([F[g](xs) for g in grados])
        etr = [mean_absolute_error(tr.ventas, F[g](tr.tv.values)) for g in grados]
        ete = [mean_absolute_error(te[te.tv.between(xs[0], xs[-1])].ventas, F[g](te[te.tv.between(xs[0], xs[-1])].tv.values)) for g in grados]
        grupo, ax = ejes((0, 300), (0, 32), 7.2, 5.0, "TV (miles de USD)", "Ventas (miles)", (0, 100, 200, 300), (0, 10, 20, 30))
        grupo.move_to([-3.05, -0.45, 0])
        ptr = VGroup(*[Dot(ax.c2p(a, b), radius=0.1, color=NEGRO) for a, b in zip(tr.tv, tr.ventas)])
        pte = VGroup(*[Circle(radius=0.08, color=ROJO, stroke_width=2.5).move_to(ax.c2p(a, b)) for a, b in zip(te.tv, te.ventas)])
        k = ValueTracker(0.0)

        def y_act():
            v = k.get_value()
            i = int(min(np.floor(v), len(grados) - 2))
            f = v - i
            return (1 - f) * Ys[i] + f * Ys[i + 1]

        cu = always_redraw(lambda: curva(ax, xs, y_act(), 0, 32, AZUL, 5))
        lim = 6.5
        g2, ax2 = ejes((0, len(grados) - 1), (0, lim), 4.3, 3.4, "grado del polinomio", "error medio", (), (0, 3, 6))
        g2.move_to([4.2, -0.75, 0])
        for i, g in enumerate(grados):
            g2.add(T(str(g), 22, GRIS).next_to(ax2.c2p(i, 0), DOWN, buff=0.14))
        tit = always_redraw(lambda: VGroup(T("Grado", 26, GRIS), Z(str(grados[int(round(k.get_value()))]), 56, AZUL)).arrange(RIGHT, buff=0.25).move_to([4.2, 2.0, 0]))
        self.play(Create(grupo), run_time=1)
        self.play(LaggedStart(*[GrowFromCenter(p) for p in ptr], lag_ratio=0.05), run_time=1.1)
        n0 = T("13 mercados para entrenar", 28).move_to([-2.9, 2.3, 0], aligned_edge=LEFT)
        self.play(FadeIn(n0), FadeIn(g2), FadeIn(tit), Create(cu), run_time=1.2)
        self.cue()
        self.wait(1)
        ltr, lte = VGroup(), VGroup()
        self.add(ltr, lte)
        c = lambda v: min(v, lim)

        def agrega(i):
            p = ax2.c2p(i, c(etr[i]))
            ltr.add(Dot(p, radius=0.07, color=NEGRO))
            if i > 0:
                ltr.add(Line(ax2.c2p(i - 1, c(etr[i - 1])), p, color=NEGRO, stroke_width=4))

        agrega(0)
        for i in range(1, len(grados)):
            self.play(k.animate.set_value(i), run_time=1.5, rate_func=smooth)
            agrega(i)
            self.wait(0.45)
            if i in (2, 5, len(grados) - 1):
                self.cue()
        self.play(FadeOut(n0))
        n1 = T("Pasa por todos sus puntos", 28).move_to([-2.9, 2.3, 0], aligned_edge=LEFT)
        self.play(FadeIn(n1))
        self.wait(1.2)
        self.play(FadeOut(n1))
        n2 = T("Ahora los mercados que no vio", 28, ROJO, BOLD).move_to([-2.9, 2.3, 0], aligned_edge=LEFT)
        self.play(FadeIn(n2), LaggedStart(*[FadeIn(p, scale=0.4) for p in pte], lag_ratio=0.02), run_time=1.6)
        self.cue()
        anims = []
        for i in range(len(grados)):
            pt = ax2.c2p(i, c(ete[i]))
            anims.append(GrowFromCenter(Dot(pt, radius=0.07, color=ROJO)))
            if i > 0:
                anims.append(Create(Line(ax2.c2p(i - 1, c(ete[i - 1])), pt, color=ROJO, stroke_width=4)))
        self.play(LaggedStart(*anims, lag_ratio=0.35), run_time=3.4)
        e1 = T("Entrenamiento", 24, NEGRO, BOLD).move_to(ax2.c2p(1.7, 0.75))
        e2 = T("Prueba", 24, ROJO, BOLD).move_to(ax2.c2p(2.7, 5.0))
        self.play(FadeIn(e1), FadeIn(e2))
        if max(ete) > lim:
            self.play(FadeIn(T("sigue subiendo", 20, ROJO, BOLD).next_to(ax2.c2p(len(grados) - 1, lim), UP, buff=0.12).shift(LEFT * 0.7)))
        self.cue()
        self.wait(3)


class Frenos:
    """Datos comunes de Ridge y Lasso: 12 mercados y un polinomio de grado 9."""
    tr, te = muestra(12, 3)
    G = 9
    u = staticmethod(lambda x: (np.asarray(x, float) - 150) / 150)

    @classmethod
    def X(cls, x):
        u = cls.u(x)
        return np.column_stack([u ** i for i in range(1, cls.G + 1)])


class EscenaFreno(Escena):
    modo, formula, color_barra = "ridge", "", ROJO

    def path(self):
        X0 = Frenos.X(Frenos.tr.tv.values)
        self.mu, self.sd = X0.mean(0), X0.std(0)
        X = (X0 - self.mu) / self.sd
        y = Frenos.tr.ventas.values
        self.ym = y.mean()
        yc = y - self.ym
        n = len(y)
        if self.modo == "ridge":
            ls = np.logspace(-9, 3.2, 90)
            C = [np.linalg.solve(X.T @ X + l * n * np.eye(X.shape[1]), X.T @ yc) for l in ls]
        else:
            ls = np.logspace(-3.4, 1.05, 90)
            C = []
            m = Lasso(alpha=ls[-1], warm_start=True, max_iter=800000, tol=1e-7, fit_intercept=False)
            for l in ls[::-1]:
                m.alpha = l
                m.fit(X, yc)
                C.append(m.coef_.copy())
            C = C[::-1]
        return ls, np.array(C)

    def construct(self):
        ls, C = self.path()
        xs = np.linspace(Frenos.tr.tv.min(), Frenos.tr.tv.max(), 200)
        Xg = (Frenos.X(xs) - self.mu) / self.sd
        grupo, ax = ejes((0, 300), (0, 32), 6.4, 4.6, "TV (miles de USD)", "Ventas", (0, 100, 200, 300), (0, 10, 20, 30))
        grupo.move_to([-3.55, -0.1, 0])
        ptr = VGroup(*[Dot(ax.c2p(a, b), radius=0.1, color=NEGRO) for a, b in zip(Frenos.tr.tv, Frenos.tr.ventas)])
        k = ValueTracker(0.0)
        n = len(ls)

        def co():
            v = k.get_value() * (n - 1)
            i = int(min(np.floor(v), n - 2))
            f = v - i
            return (1 - f) * C[i] + f * C[i + 1]

        cu = always_redraw(lambda: curva(ax, xs, self.ym + Xg @ co(), 0, 32, AZUL, 5))
        # Barras de coeficientes en escala comprimida para que quepan el antes y el después
        base_y = 0.05
        escala = lambda b: np.sign(b) * np.log10(1 + abs(b) * 4) * 0.34
        px = [1.05 + i * 0.66 for i in range(Frenos.G)]
        cero = Line([0.7, base_y, 0], [px[-1] + 0.35, base_y, 0], color=NEGRO, stroke_width=2)
        nom = VGroup(*[T("x" + ("" if i == 0 else "²³⁴⁵⁶⁷⁸⁹"[i - 1]), 24, GRIS).move_to([px[i], -2.25, 0]) for i in range(Frenos.G)])

        def barras():
            g = VGroup()
            for i, b in enumerate(co()):
                if abs(b) < 1e-6:
                    g.add(T("0", 28, GRIS, BOLD).move_to([px[i], base_y, 0]))
                    continue
                h = float(escala(b))
                h = np.clip(h, -1.9, 1.6)
                g.add(Rectangle(width=0.42, height=max(abs(h), 0.02)).set_stroke(width=0).set_fill(self.color_barra, 1).move_to([px[i], base_y + h / 2, 0]))
            return g

        bars = always_redraw(barras)
        f = T(self.formula, 36, NEGRO).move_to([2.9, 2.35, 0])
        lx0, lx1 = -6.3, -0.8
        lin = Line([lx0, -3.35, 0], [lx1, -3.35, 0], color=CLARO, stroke_width=8)
        perilla = always_redraw(lambda: Circle(radius=0.17, color=ROJO, fill_opacity=1).move_to([lx0 + (lx1 - lx0) * k.get_value(), -3.35, 0]))
        tl = T("λ", 34, ROJO, BOLD).next_to(lin, LEFT, buff=0.2)
        t0 = T("sin freno", 22, GRIS).next_to(lin, DOWN, buff=0.15).align_to(lin, LEFT)
        t1 = T("mucho freno", 22, GRIS).next_to(lin, DOWN, buff=0.15).align_to(lin, RIGHT)
        vivas = always_redraw(lambda: VGroup(T("Columnas vivas", 26, GRIS), Z(f"{int((np.abs(co()) >= 1e-6).sum())} de {Frenos.G}", 42, ROJO)).arrange(RIGHT, buff=0.3).move_to([3.5, -3.1, 0]))
        tb = T("Tamaño de cada coeficiente", 26, GRIS).move_to([3.55, 1.85, 0])
        self.play(Create(grupo), run_time=0.8)
        self.play(LaggedStart(*[GrowFromCenter(p) for p in ptr], lag_ratio=0.05), run_time=0.9)
        self.play(Create(cu), run_time=1)
        self.cue()
        self.wait(0.8)
        self.play(FadeIn(cero), FadeIn(nom), FadeIn(bars), FadeIn(tb), run_time=1)
        self.cue()
        self.wait(0.8)
        self.play(Write(f), run_time=1.3)
        self.play(FadeIn(lin), FadeIn(perilla), FadeIn(tl), FadeIn(t0), FadeIn(t1), FadeIn(vivas))
        self.cue()
        self.wait(1.2)
        self.mover(k)
        cierre = self.cierre()
        self.play(FadeOut(tb), FadeIn(cierre, shift=UP * 0.2))
        self.cue()
        self.wait(3)


class S5Ridge(EscenaFreno):
    modo, formula, color_barra = "ridge", "costo = error + λ · suma de b²", ROJO

    def mover(self, k):
        self.play(k.animate.set_value(0.47), run_time=4.5, rate_func=smooth)
        self.cue()
        self.wait(1)
        self.play(k.animate.set_value(0.93), run_time=4.5, rate_func=smooth)
        self.cue()
        self.wait(0.8)
        self.play(k.animate.set_value(0.52), run_time=2.2, rate_func=smooth)
        self.cue()

    def cierre(self):
        return T("Todas se encogen. Ninguna desaparece.", 25, ROJO, BOLD).move_to([3.45, 1.85, 0])


class S6Lasso(EscenaFreno):
    modo, formula, color_barra = "lasso", "costo = error + λ · suma de |b|", NEGRO

    def mover(self, k):
        self.play(k.animate.set_value(0.42), run_time=5, rate_func=linear)
        self.cue()
        self.wait(0.8)
        self.play(k.animate.set_value(0.85), run_time=5, rate_func=linear)
        self.cue()
        self.wait(0.8)

    def cierre(self):
        return T("Las que no pagan su costo valen cero.", 25, ROJO, BOLD).move_to([3.45, 1.85, 0])


class S7Geometria(Escena):
    """El círculo roza las curvas de error en cualquier punto. El rombo las toca en una esquina."""

    def construct(self):
        Q = np.array([[1.0, 0.45], [0.45, 1.9]])
        bh = np.array([2.35, 0.62])
        lams = np.linspace(0, 7.5, 240)
        rid = np.array([np.linalg.solve(Q + l * np.eye(2), Q @ bh) for l in lams])

        def cd(l):
            b = bh.copy()
            for _ in range(300):
                for j in (0, 1):
                    o = 1 - j
                    r = Q[j, j] * bh[j] + Q[j, o] * (bh[o] - b[o])
                    b[j] = np.sign(r) * max(abs(r) - l / 2, 0) / Q[j, j]
            return b

        las = np.array([cd(l) for l in lams * 0.9])
        tr, tl = np.linalg.norm(rid, axis=1), np.abs(las).sum(1)
        sq = np.linalg.cholesky(np.linalg.inv(Q))

        def panel(c):
            g = ejes((-1.2, 3.2), (-1.2, 3.2), 5.1, 5.1, "", "", (), (), marco=False)
            g[0].move_to([c, -0.55, 0])
            return g

        (g1, a1), (g2, a2) = panel(-3.6), panel(3.6)

        def cruz(ax, c):
            return VGroup(DashedLine(ax.c2p(-1.2, 0), ax.c2p(3.2, 0), color=CLARO), DashedLine(ax.c2p(0, -1.2), ax.c2p(0, 3.2), color=CLARO))

        marco = VGroup()
        for ax in (a1, a2):
            ax.x_axis.set_opacity(0)
            ax.y_axis.set_opacity(0)
            marco.add(Line(ax.c2p(-1.2, 0), ax.c2p(3.2, 0), color=NEGRO, stroke_width=2), Line(ax.c2p(0, -1.2), ax.c2p(0, 3.2), color=NEGRO, stroke_width=2))
            marco.add(T("b₁", 26, GRIS).next_to(ax.c2p(3.2, 0), UP, buff=0.1), T("b₂", 26, GRIS).next_to(ax.c2p(0, 3.2), RIGHT, buff=0.1))

        def elipse(ax, nivel, color=CLARO, ancho=2.5):
            t = np.linspace(0, 2 * np.pi, 120)
            pts = np.array([bh + np.sqrt(nivel) * sq @ np.array([np.cos(a), np.sin(a)]) for a in t])
            return VMobject(stroke_color=color, stroke_width=ancho).set_points_as_corners([ax.c2p(*p) for p in pts])

        fondo = VGroup(*[elipse(a, n) for a in (a1, a2) for n in (0.5, 2.0, 4.5)])
        s = ValueTracker(0.17)
        ind = lambda: int(s.get_value() * (len(lams) - 1))

        def nivel(b):
            d = b - bh
            return float(d @ Q @ d)

        reg1 = always_redraw(lambda: Circle(radius=(a1.c2p(tr[ind()], 0)[0] - a1.c2p(0, 0)[0]), color=ROJO, stroke_width=3, fill_opacity=0.14).move_to(a1.c2p(0, 0)))

        def rombo():
            t = tl[ind()]
            return Polygon(a2.c2p(t, 0), a2.c2p(0, t), a2.c2p(-t, 0), a2.c2p(0, -t), color=NEGRO, stroke_width=3, fill_opacity=0.12)

        reg2 = always_redraw(rombo)
        el1 = always_redraw(lambda: elipse(a1, max(nivel(rid[ind()]), 1e-4), AZUL, 4))
        el2 = always_redraw(lambda: elipse(a2, max(nivel(las[ind()]), 1e-4), AZUL, 4))
        p1 = always_redraw(lambda: Dot(a1.c2p(*rid[ind()]), radius=0.11, color=ROJO))
        p2 = always_redraw(lambda: Dot(a2.c2p(*las[ind()]), radius=0.11, color=ROJO))
        est = VGroup(*[Dot(a.c2p(*bh), radius=0.09, color=AZUL) for a in (a1, a2)])
        tit1 = Z("RIDGE", 40, ROJO).move_to([-3.6, 2.42, 0])
        tit2 = Z("LASSO", 40, NEGRO).move_to([3.6, 2.42, 0])
        self.play(FadeIn(marco), FadeIn(fondo), FadeIn(est), FadeIn(tit1), FadeIn(tit2), run_time=1)
        n0 = T("Azul: los coeficientes sin freno", 28, AZUL, BOLD).move_to([0, -3.6, 0])
        self.play(FadeIn(n0))
        self.cue()
        self.wait(1.2)
        self.play(FadeOut(n0))
        n1 = T("La zona es el presupuesto para los coeficientes", 28).move_to([0, -3.6, 0])
        self.play(FadeIn(reg1), FadeIn(reg2), FadeIn(el1), FadeIn(el2), FadeIn(p1), FadeIn(p2), FadeIn(n1))
        self.cue()
        self.wait(1.2)
        self.play(s.animate.set_value(0.3), run_time=4, rate_func=smooth)
        self.wait(0.6)
        self.play(FadeOut(n1))
        n2 = T("El punto rojo es el mejor ajuste que cabe en el presupuesto", 28).move_to([0, -3.6, 0])
        self.play(FadeIn(n2))
        self.play(s.animate.set_value(0.58), run_time=3.6, rate_func=smooth)
        self.cue()
        self.wait(0.8)
        self.play(FadeOut(n2))
        v = rid[ind()]
        tx1 = T(f"b₂ = {v[1]:.2f}".replace(".", ",") + ", chico pero vivo", 28, ROJO, BOLD).move_to([-3.6, -3.6, 0])
        tx2 = T("b₂ = 0: la esquina la elimina", 28, NEGRO, BOLD).move_to([3.6, -3.6, 0])
        an = Circle(radius=0.34, color=ROJO, stroke_width=4).move_to(a2.c2p(*las[ind()]))
        self.play(FadeIn(tx1))
        self.cue()
        self.play(FadeIn(tx2), Create(an))
        self.cue()
        self.wait(3.5)


class S8Validacion(Escena):
    """Cinco turnos de validación eligen el freno sin tocar la prueba."""

    def construct(self):
        C = ["tv", "radio", "prensa"]
        tr, te = train_test_split(df, test_size=0.25, random_state=42)
        kf = KFold(5, shuffle=True, random_state=42)
        al = np.array([0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0])
        ev = []
        for a in al:
            p = make_pipeline(PolynomialFeatures(5, include_bias=False), StandardScaler(), Lasso(alpha=a, max_iter=300000))
            ev.append(-cross_val_score(p, tr[C], tr.ventas, cv=kf, scoring="neg_mean_absolute_error").mean())
        ev = np.array(ev)
        ancho, alto = 0.86, 0.58
        filas = VGroup()
        for i in range(5):
            f = VGroup(*[Rectangle(width=ancho, height=alto).set_stroke(WHITE, 3).set_fill(ROJO if j == i else CLARO, 1).move_to([-6.1 + j * ancho, 1.6 - i * (alto + 0.14), 0]) for j in range(5)])
            filas.add(f)
        cab = T("150 mercados en 5 partes", 26, GRIS).next_to(filas, UP, buff=0.2).align_to(filas, LEFT)
        ley = VGroup(Square(0.26).set_stroke(width=0).set_fill(CLARO, 1), T("entrena", 24, GRIS), Square(0.26).set_stroke(width=0).set_fill(ROJO, 1), T("valida", 24, GRIS)).arrange(RIGHT, buff=0.16).next_to(filas, DOWN, buff=0.3).align_to(filas, LEFT)
        lg = np.log10(al)
        tope = max(ev.max() * 1.1, 1.2)
        g2, ax = ejes((lg[0], lg[-1]), (0, tope), 6.9, 3.95, "fuerza del freno α (escala logarítmica)", "error medio en validación", (), (0, 0.5, 1.0), fmt=lambda v: f"{v:.1f}".replace(".", ","))
        g2.move_to([2.75, -0.6, 0])
        self.play(FadeIn(cab), FadeIn(ley), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(f, shift=RIGHT * 0.2) for f in filas], lag_ratio=0.35), run_time=2.6)
        self.cue()
        self.wait(0.6)
        self.play(FadeIn(g2))
        marca = SurroundingRectangle(filas[0], color=NEGRO, buff=0.05, stroke_width=3)
        self.play(Create(marca))
        pts = VGroup()
        self.add(pts)
        for f in range(1, 5):
            self.play(marca.animate.move_to(filas[f]), run_time=0.4)
        self.play(marca.animate.move_to(filas[0]), run_time=0.3)
        p0 = Dot(ax.c2p(lg[0], ev[0]), radius=0.09, color=ROJO)
        self.play(GrowFromCenter(p0))
        n = T("Cada punto es el promedio de los cinco turnos", 26).move_to([6.6, 2.42, 0], aligned_edge=RIGHT)
        self.play(FadeIn(n))
        self.cue()
        self.wait(0.9)
        prev = p0
        for i in range(1, len(al)):
            self.play(marca.animate.move_to(filas[i % 5]), run_time=0.14)
            d = Dot(ax.c2p(lg[i], ev[i]), radius=0.09, color=ROJO)
            s = Line(ax.c2p(lg[i - 1], ev[i - 1]), ax.c2p(lg[i], ev[i]), color=ROJO, stroke_width=4)
            self.play(Create(s), GrowFromCenter(d), run_time=0.34)
        self.cue()
        self.play(FadeOut(marca), FadeOut(n))
        m = int(ev.argmin())
        an = Circle(radius=0.28, color=NEGRO, stroke_width=4).move_to(ax.c2p(lg[m], ev[m]))
        t = T(f"α = {al[m]:g}".replace(".", ","), 30, NEGRO, BOLD).next_to(an, UP, buff=0.25)
        t2 = T("Aquí se elige. La prueba sigue guardada.", 28, ROJO, BOLD).move_to([6.6, 2.42, 0], aligned_edge=RIGHT)
        self.play(Create(an), FadeIn(t), FadeIn(t2))
        self.cue()
        self.wait(3)
