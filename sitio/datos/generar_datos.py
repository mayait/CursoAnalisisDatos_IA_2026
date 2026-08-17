#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la base de datos del curso: Comercial Andina.

Un distribuidor ecuatoriano ficticio con tiendas en cinco ciudades y canal en línea.
Los datos son sintéticos pero están construidos para que aparezcan, de forma natural,
los fenómenos que cada semana del curso necesita enseñar:

  Semana 3  · el ticket es bimodal (minorista y mayorista): la media no describe a nadie
  Semana 4  · nulos, duplicados, fechas en texto, ciudades mal escritas, cantidades negativas
  Semana 5  · cinco tablas con granularidades distintas y una unión que puede duplicar filas
  Semana 6  · estacionalidad y diferencias entre ciudades que se ven en un gráfico
  Semana 8  · estructura RFM+P real, con clientes VIP, leales, en riesgo y perdidos
  Semana 9  · un experimento A/B y una paradoja de Simpson entre canal y segmento
  Semana 12 · relación de inversión publicitaria mensual con ventas
  Semana 14 · abandono de clientes con clases desbalanceadas (~13 %)

Todo sale de una única semilla, así que el resultado es idéntico en cualquier máquina.

Uso:  python3 generar_datos.py
"""
import os
import numpy as np
import pandas as pd

SEED = 42
rng = np.random.default_rng(SEED)
AQUI = os.path.dirname(os.path.abspath(__file__))

INICIO = pd.Timestamp("2024-01-01")
FIN = pd.Timestamp("2026-06-30")

CIUDADES = ["Quito", "Guayaquil", "Cuenca", "Manta", "Loja"]
PESO_CIUDAD = [0.38, 0.27, 0.15, 0.12, 0.08]

# ── SUCURSALES ────────────────────────────────────────────────
def gen_sucursales():
    filas = []
    for i, c in enumerate(CIUDADES, 1):
        filas.append(dict(sucursal_id=f"S{i:02d}", ciudad=c, canal="Tienda",
                          fecha_apertura=(INICIO - pd.Timedelta(days=int(rng.integers(400, 3000)))).date(),
                          metros_cuadrados=int(rng.integers(120, 640))))
    filas.append(dict(sucursal_id="S99", ciudad="Nacional", canal="Online",
                      fecha_apertura=pd.Timestamp("2024-03-01").date(), metros_cuadrados=0))
    return pd.DataFrame(filas)

# ── PRODUCTOS ─────────────────────────────────────────────────
CATALOGO = [
    ("Bebidas", "Gaseosas", 0.55, 1.10), ("Bebidas", "Aguas", 0.30, 0.75),
    ("Bebidas", "Jugos", 0.70, 1.55), ("Abarrotes", "Arroz", 0.90, 1.45),
    ("Abarrotes", "Aceites", 1.80, 2.90), ("Abarrotes", "Enlatados", 1.10, 1.95),
    ("Limpieza", "Detergentes", 2.20, 3.80), ("Limpieza", "Desinfectantes", 1.60, 2.95),
    ("Cuidado personal", "Higiene bucal", 1.40, 2.60), ("Cuidado personal", "Shampoo", 2.80, 5.20),
    ("Snacks", "Galletas", 0.45, 0.95), ("Snacks", "Frituras", 0.60, 1.25),
]

def gen_productos():
    filas = []
    pid = 1
    for cat, sub, costo, precio in CATALOGO:
        for k in range(rng.integers(4, 9)):
            fc = float(rng.normal(1.0, 0.16))
            fc = min(max(fc, 0.7), 1.4)
            filas.append(dict(
                producto_id=f"P{pid:04d}",
                nombre=f"{sub} {chr(65 + k)}",
                categoria=cat, subcategoria=sub,
                costo_unitario=round(costo * fc, 2),
                precio_lista=round(precio * fc, 2)))
            pid += 1
    return pd.DataFrame(filas)

# ── CLIENTES ──────────────────────────────────────────────────
def gen_clientes(n=1800):
    ciudad = rng.choice(CIUDADES, size=n, p=PESO_CIUDAD)
    # el 22 % son mayoristas: compran mucho más por factura (origen de la bimodalidad)
    tipo = rng.choice(["Minorista", "Mayorista"], size=n, p=[0.78, 0.22])
    alta = INICIO + pd.to_timedelta(rng.integers(-900, 700, size=n), unit="D")
    canal = rng.choice(["Visita comercial", "Referido", "Redes sociales", "Punto de venta"],
                       size=n, p=[0.22, 0.24, 0.19, 0.35])
    return pd.DataFrame(dict(
        cliente_id=[f"C{i:05d}" for i in range(1, n + 1)],
        razon_social=[f"Cliente {i:05d}" for i in range(1, n + 1)],
        ciudad=ciudad, tipo_cliente=tipo,
        fecha_alta=[d.date() for d in alta], canal_captacion=canal))

# ── VENTAS ────────────────────────────────────────────────────
def estacionalidad(fecha):
    """Diciembre y mayo altos, febrero bajo. Tendencia suave al alza."""
    mes = fecha.month
    est = {1: .88, 2: .82, 3: .95, 4: .98, 5: 1.12, 6: 1.0,
           7: 1.02, 8: .97, 9: .99, 10: 1.04, 11: 1.08, 12: 1.30}[mes]
    meses = (fecha.year - 2024) * 12 + mes - 1
    return est * (1 + 0.004 * meses)

def gen_ventas(clientes, productos, sucursales):
    filas = []
    factura = 100000
    prods = productos.to_dict("records")
    sucs_tienda = sucursales[sucursales.canal == "Tienda"].set_index("ciudad")["sucursal_id"].to_dict()

    for cli in clientes.to_dict("records"):
        mayorista = cli["tipo_cliente"] == "Mayorista"
        # intensidad de compra y fecha de abandono: aquí nacen R, F, M y el churn
        base_freq = rng.gamma(3.2 if mayorista else 2.0, 3.0 if mayorista else 2.4)
        abandona = rng.random() < (0.10 if mayorista else 0.15)
        fin_cliente = FIN - pd.Timedelta(days=int(rng.integers(120, 500))) if abandona else FIN
        inicio_cliente = max(pd.Timestamp(cli["fecha_alta"]), INICIO)
        if fin_cliente <= inicio_cliente:
            continue
        dias = (fin_cliente - inicio_cliente).days
        n_fac = max(1, int(base_freq * dias / 365))

        for _ in range(n_fac):
            fecha = inicio_cliente + pd.Timedelta(days=int(rng.integers(0, max(dias, 1))))
            if rng.random() > estacionalidad(fecha) / 1.30:
                continue
            online = rng.random() < (0.34 if not mayorista else 0.16)
            suc = "S99" if online else sucs_tienda.get(cli["ciudad"], "S01")
            factura += 1
            n_lineas = int(rng.integers(2, 7 if not mayorista else 12))
            for _ in range(n_lineas):
                p = prods[int(rng.integers(0, len(prods)))]
                cant = int(rng.integers(1, 5)) if not mayorista else int(rng.integers(8, 60))
                desc = float(np.round(rng.choice([0, 0, 0, .05, .10, .15],
                                                 p=[.55, .12, .08, .12, .08, .05]), 2))
                filas.append(dict(
                    factura_id=f"F{factura}", fecha=fecha.date(),
                    cliente_id=cli["cliente_id"], sucursal_id=suc,
                    producto_id=p["producto_id"], cantidad=cant,
                    precio_unitario=p["precio_lista"], descuento=desc,
                    es_devolucion=False))
    v = pd.DataFrame(filas)

    # devoluciones: 2.4 % de las líneas, con cantidad negativa y marca explícita
    idx = rng.choice(v.index, size=int(len(v) * 0.024), replace=False)
    dev = v.loc[idx].copy()
    dev["cantidad"] = -dev["cantidad"]
    dev["es_devolucion"] = True
    dev["factura_id"] = "C" + dev["factura_id"].str[1:]
    dev["fecha"] = pd.to_datetime(dev["fecha"]) + pd.to_timedelta(
        rng.integers(2, 20, size=len(dev)), unit="D")
    dev["fecha"] = dev["fecha"].dt.date
    v = pd.concat([v, dev], ignore_index=True)
    return v.sort_values(["fecha", "factura_id"]).reset_index(drop=True)

# ── SUCIEDAD DELIBERADA (semana 4) ────────────────────────────
def ensuciar(v):
    v = v.copy()
    n = len(v)

    # 1) 7.8 % de líneas sin identificador de cliente
    idx = rng.choice(n, size=int(n * 0.078), replace=False)
    v.loc[idx, "cliente_id"] = np.nan

    # 2) 1.3 % de filas duplicadas exactas
    dup = v.sample(n=int(n * 0.013), random_state=SEED)
    v = pd.concat([v, dup], ignore_index=True)

    # 3) fechas: el 12 % queda como texto en formato dd/mm/aaaa
    v["fecha"] = v["fecha"].astype(str)
    idx = rng.choice(len(v), size=int(len(v) * 0.12), replace=False)
    v.loc[idx, "fecha"] = pd.to_datetime(v.loc[idx, "fecha"]).dt.strftime("%d/%m/%Y")

    # 4) 0.6 % de cantidades negativas SIN marca de devolución (error real, no devolución)
    cand = v[~v["es_devolucion"]].index
    idx = rng.choice(cand, size=int(len(cand) * 0.006), replace=False)
    v.loc[idx, "cantidad"] = -v.loc[idx, "cantidad"].abs()

    # 5) precios extremos: 0.2 % con un cero de más al teclear
    idx = rng.choice(len(v), size=max(8, int(len(v) * 0.002)), replace=False)
    v.loc[idx, "precio_unitario"] = v.loc[idx, "precio_unitario"] * 10

    # 6) 0.4 % de precios ausentes
    idx = rng.choice(len(v), size=int(len(v) * 0.004), replace=False)
    v.loc[idx, "precio_unitario"] = np.nan

    return v.sample(frac=1, random_state=SEED).reset_index(drop=True)

def ensuciar_clientes(c):
    c = c.copy()
    # ciudad escrita de cuatro formas distintas en el 9 % de los registros
    idx = rng.choice(len(c), size=int(len(c) * 0.09), replace=False)
    variantes = {"Quito": ["quito", "QUITO", "Quito ", " Quito"],
                 "Guayaquil": ["guayaquil", "GUAYAQUIL", "Guayaquil ", "Guayaquíl"],
                 "Cuenca": ["cuenca", "CUENCA", "Cuenca ", " cuenca"],
                 "Manta": ["manta", "MANTA", "Manta ", " Manta"],
                 "Loja": ["loja", "LOJA", "Loja ", " Loja"]}
    for i in idx:
        orig = c.at[i, "ciudad"]
        c.at[i, "ciudad"] = variantes[orig][int(rng.integers(0, 4))]
    # 3 % sin fecha de alta
    idx = rng.choice(len(c), size=int(len(c) * 0.03), replace=False)
    c.loc[idx, "fecha_alta"] = np.nan
    return c

# ── EXPERIMENTO A/B Y PARADOJA DE SIMPSON (semana 9) ──────────
def gen_experimento(clientes):
    """Campaña de reactivación por correo.

    Global: el grupo de control convierte MÁS que el tratamiento.
    Por segmento: el tratamiento convierte más en minoristas Y en mayoristas.
    La inversión se produce porque la asignación quedó desbalanceada por segmento.
    """
    c = clientes.sample(frac=1, random_state=SEED).reset_index(drop=True)
    filas = []
    for r in c.to_dict("records"):
        may = r["tipo_cliente"] == "Mayorista"
        # asignación sesgada: los mayoristas cayeron sobre todo en control
        p_trat = 0.20 if may else 0.75
        grupo = "Tratamiento" if rng.random() < p_trat else "Control"
        # los mayoristas convierten mucho más, en cualquier grupo
        base = 0.45 if may else 0.08
        p = base + (0.04 if grupo == "Tratamiento" else 0.0)
        filas.append(dict(cliente_id=r["cliente_id"], tipo_cliente=r["tipo_cliente"],
                          ciudad=r["ciudad"], grupo=grupo,
                          convirtio=int(rng.random() < p)))
    return pd.DataFrame(filas)

# ── INVERSIÓN PUBLICITARIA MENSUAL (semana 12) ────────────────
def gen_marketing(ventas):
    v = ventas.copy()
    v["fecha"] = pd.to_datetime(v["fecha"], errors="coerce")
    v = v.dropna(subset=["fecha"])
    v["monto"] = v["cantidad"] * v["precio_unitario"] * (1 - v["descuento"])
    mens = v.groupby(v["fecha"].dt.to_period("M"))["monto"].sum().reset_index()
    mens["mes"] = mens["fecha"].dt.to_timestamp().dt.date
    n = len(mens)
    radio = np.round(rng.uniform(400, 2600, n), 0)
    digital = np.round(rng.uniform(900, 6800, n), 0)
    # las ventas reales ya existen; la inversión se construye correlacionada con ellas
    v_norm = (mens["monto"] - mens["monto"].mean()) / mens["monto"].std()
    volantes = np.round(np.clip(1500 + 620 * v_norm + rng.normal(0, 180, n), 120, None), 0)
    return pd.DataFrame(dict(mes=mens["mes"], inversion_radio=radio,
                             inversion_digital=digital, inversion_volantes=volantes,
                             ventas_mes=mens["monto"].round(2)))

# ── MAIN ──────────────────────────────────────────────────────
def main():
    sucursales = gen_sucursales()
    productos = gen_productos()
    clientes = gen_clientes()
    ventas = gen_ventas(clientes, productos, sucursales)
    marketing = gen_marketing(ventas)
    experimento = gen_experimento(clientes)

    ventas_sucias = ensuciar(ventas)
    clientes_sucios = ensuciar_clientes(clientes)

    salidas = {
        "ventas.csv": ventas_sucias,
        "ventas_limpias.csv": ventas,
        "clientes.csv": clientes_sucios,
        "productos.csv": productos,
        "sucursales.csv": sucursales,
        "marketing_mensual.csv": marketing,
        "experimento_reactivacion.csv": experimento,
    }
    for nombre, df in salidas.items():
        df.to_csv(os.path.join(AQUI, nombre), index=False, encoding="utf-8")
        print(f"{nombre:34s} {len(df):>7,} filas × {df.shape[1]} columnas")

    # comprobaciones de que los fenómenos didácticos están presentes
    v = ventas.copy()
    v["monto"] = v["cantidad"] * v["precio_unitario"] * (1 - v["descuento"])
    tic = v[~v.es_devolucion].groupby("factura_id")["monto"].sum()
    print("\nComprobaciones didácticas")
    print(f"  ticket medio {tic.mean():8.2f} · mediana {tic.median():8.2f} "
          f"· razón {tic.mean()/tic.median():.2f} (bimodalidad)")
    ex = experimento
    g = ex.groupby("grupo")["convirtio"].mean()
    print(f"  A/B global: control {g['Control']:.3f} vs tratamiento {g['Tratamiento']:.3f} "
          f"({'control gana' if g['Control'] > g['Tratamiento'] else 'tratamiento gana'})")
    por = ex.groupby(["tipo_cliente", "grupo"])["convirtio"].mean().unstack()
    for t in por.index:
        print(f"    {t:11s}: control {por.loc[t,'Control']:.3f} vs "
              f"tratamiento {por.loc[t,'Tratamiento']:.3f}")
    vs = ventas_sucias
    print(f"  calidad: {vs.cliente_id.isna().mean():.1%} sin cliente · "
          f"{vs.duplicated().mean():.1%} duplicados · "
          f"{vs.precio_unitario.isna().mean():.1%} sin precio")
    ult = pd.to_datetime(ventas.fecha).max()
    rec = ventas.groupby("cliente_id").fecha.max()
    print(f"  RFM: {len(rec):,} clientes con compras · "
          f"{(pd.to_datetime(rec) < ult - pd.Timedelta(days=180)).mean():.1%} inactivos +180 días")

if __name__ == "__main__":
    main()
