#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera andina_market.csv: la filial ecuatoriana de Superstore, con problemas
de calidad SEMBRADOS y documentados. Complementa superstore.xlsx (limpio).

Problemas sembrados (la clave exacta queda en clave.json y clave_problemas.md):
 P1  ~10% de líneas sin ID Cliente (mezcla: NaN, cadena vacía, "SIN-ID")
 P2  Duplicados exactos (filas repetidas)
 P3  Fechas como TEXTO en formatos mezclados (yyyy-mm-dd y dd/mm/yyyy)
 P4  Fechas imposibles: envío anterior al pedido
 P5  Ventas como texto con "$" y coma decimal en algunas filas → columna object
 P6  Ciudad inconsistente (QUITO / quito / " Quito" / Sto. Domingo…)
 P7  Descuento: NaN (no registrado) conviviendo con 0 legítimo
 P8  Cantidad negativa (devoluciones sin marcar)
 P9  Utilidad con centinela -9999 (desconocido codificado)
 P10 Provincia con nulos
 P11 Granularidad: "Total Pedido" repetido en cada línea (trampa de doble conteo)
"""
import json
import numpy as np
import pandas as pd
from pathlib import Path

AQUI = Path(__file__).resolve().parent
rng = np.random.default_rng(2003)

# ── Universo ─────────────────────────────────────────────────────────────
CIUDADES = [
    ("Quito", "Pichincha", "Sierra", 0.24),
    ("Guayaquil", "Guayas", "Costa", 0.26),
    ("Cuenca", "Azuay", "Sierra", 0.10),
    ("Manta", "Manabí", "Costa", 0.08),
    ("Ambato", "Tungurahua", "Sierra", 0.07),
    ("Loja", "Loja", "Sierra", 0.05),
    ("Santo Domingo", "Santo Domingo de los Tsáchilas", "Costa", 0.06),
    ("Machala", "El Oro", "Costa", 0.05),
    ("Portoviejo", "Manabí", "Costa", 0.04),
    ("Puerto Ayora", "Galápagos", "Galápagos", 0.03),
    ("Tena", "Napo", "Amazonía", 0.02),
]
CATALOGO = [
    ("Tecnología", "Teléfonos", ["Teléfono Nokia C32", "Samsung Galaxy A15", "Xiaomi Redmi 13"]),
    ("Tecnología", "Accesorios", ["Audífonos JBL Tune", "Mouse Logitech M170", "Teclado Genius KB-100", "Cargador Anker 20W"]),
    ("Tecnología", "Copiadoras", ["Copiadora Epson EcoTank L3250", "Impresora HP Smart Tank 515"]),
    ("Mobiliario", "Sillas", ["Silla ejecutiva Ofix", "Silla plegable Rimax"]),
    ("Mobiliario", "Mesas", ["Mesa de reuniones 180cm", "Escritorio en L Maderkit"]),
    ("Mobiliario", "Libreros", ["Librero 5 repisas", "Estante metálico Beta"]),
    ("Suministros", "Papelería", ["Resma papel A4 75g", "Cuaderno universitario Norma", "Carpetas manila x25"]),
    ("Suministros", "Archivadores", ["Archivador Leitz A-Z", "Caja archivo x10"]),
    ("Suministros", "Arte", ["Marcadores Sharpie x12", "Cinta adhesiva Scotch x6"]),
]
NOMBRES = ["María Salazar", "José Cedeño", "Ana Tituaña", "Luis Zambrano", "Carmen Vélez",
           "Pedro Guamán", "Lucía Espinoza", "Diego Paredes", "Rosa Chiriboga", "Andrés Molina",
           "Verónica Cruz", "Jorge Intriago", "Paola Cárdenas", "Francisco Mera", "Gabriela Ponce",
           "Ramiro Quishpe", "Daniela Loor", "Esteban Riofrío", "Marcela Yépez", "Óscar Bravo",
           "Tatiana Mendoza", "Hernán Cobo", "Ivonne Macías", "Byron Toapanta", "Sofía Arteaga",
           "Patricio Alarcón", "Nadia Reinoso", "Gustavo Palma", "Elena Carrión", "Fabián Ortiz",
           "Karla Bustamante", "Milton Cajas", "Priscila Vera", "Wilson Chila", "Marta Aguirre",
           "Rodrigo Pinos", "Cynthia Baque", "Iván Sarango", "Belén Cornejo", "Héctor Anchundia"]
SEGMENTOS = ["Consumidor", "Corporativo", "PYME"]
MODOS = ["Estándar", "Segunda Clase", "Primera Clase", "Mismo Día"]
MARGEN = {"Tecnología": 0.16, "Mobiliario": 0.08, "Suministros": 0.22}

clientes = [(f"CL-{100+i}", NOMBRES[i % len(NOMBRES)], SEGMENTOS[i % 3]) for i in range(80)]
pesos_ciudad = np.array([c[3] for c in CIUDADES]); pesos_ciudad /= pesos_ciudad.sum()

# ── Pedidos y líneas (base limpia) ───────────────────────────────────────
filas = []
n_pedidos = 430
fechas_base = pd.date_range("2025-09-01", "2026-08-31", freq="D")
for p in range(n_pedidos):
    pid = f"AM-2026-{p+1:04d}"
    cid, cnom, seg = clientes[rng.integers(len(clientes))]
    ci = rng.choice(len(CIUDADES), p=pesos_ciudad)
    ciudad, prov, region = CIUDADES[ci][0], CIUDADES[ci][1], CIUDADES[ci][2]
    f_ped = fechas_base[rng.integers(len(fechas_base))]
    f_env = f_ped + pd.Timedelta(days=int(rng.integers(1, 8)))
    modo = MODOS[rng.integers(len(MODOS))]
    for _ in range(int(rng.integers(1, 6))):
        cat, sub, prods = CATALOGO[rng.integers(len(CATALOGO))]
        prod = prods[rng.integers(len(prods))]
        cant = int(rng.integers(1, 8))
        precio = float(np.round(np.exp(rng.normal(3.1, 1.0)) + 3, 2))
        desc = float(rng.choice([0.0, 0.0, 0.0, 0.1, 0.2, 0.3], p=[.30, .18, .12, .18, .14, .08]))
        venta = round(precio * cant * (1 - desc), 2)
        util = round(venta * MARGEN[cat] - venta * desc * 0.9 + rng.normal(0, 2), 2)
        filas.append([pid, f_ped, f_env, modo, cid, cnom, seg, ciudad, prov, region,
                      cat, sub, prod, cant, desc, venta, util])

df = pd.DataFrame(filas, columns=["ID Pedido", "Fecha Pedido", "Fecha Envío", "Modo Envío",
                                  "ID Cliente", "Nombre Cliente", "Segmento", "Ciudad",
                                  "Provincia", "Región", "Categoría", "Subcategoría",
                                  "Producto", "Cantidad", "Descuento", "Ventas", "Utilidad"])

# ── Pedido de ejemplo para la lección (granularidad, P11) ────────────────
ej = df["ID Pedido"] == "AM-2026-0042"
df = df[~ej].reset_index(drop=True)
cli_ej = ("CL-142", NOMBRES[2], "PYME")
lineas_ej = [("Suministros", "Papelería", "Resma papel A4 75g", 2, 0.0, 74.90, 16.48),
             ("Suministros", "Papelería", "Cuaderno universitario Norma", 3, 0.0, 52.30, 11.51),
             ("Tecnología", "Accesorios", "Mouse Logitech M170", 2, 0.0, 41.20, 6.59),
             ("Suministros", "Arte", "Cinta adhesiva Scotch x6", 1, 0.0, 19.00, 4.18)]
for cat, sub, prod, cant, desc, venta, util in lineas_ej:
    df.loc[len(df)] = ["AM-2026-0042", pd.Timestamp("2026-08-18"), pd.Timestamp("2026-08-21"),
                       "Estándar", cli_ej[0], cli_ej[1], cli_ej[2], "Puerto Ayora", "Galápagos",
                       "Galápagos", cat, sub, prod, cant, desc, venta, util]

# P11 · Total Pedido repetido en cada línea
df["Total Pedido"] = df.groupby("ID Pedido")["Ventas"].transform(lambda s: round(s.sum(), 2))

# ── Sembrar problemas ────────────────────────────────────────────────────
n = len(df)
idx = rng.permutation(n)

# P1 · sin cliente (~10%): 60 NaN + 38 "" + 20 "SIN-ID", sesgado a Costa
costa = df.index[df["Región"] == "Costa"].to_numpy()
otros = df.index[df["Región"] != "Costa"].to_numpy()
pool_sc = np.concatenate([rng.choice(costa, 74, replace=False),
                          rng.choice(otros, 44, replace=False)])
pool_sc = pool_sc[~np.isin(pool_sc, df.index[df["ID Pedido"] == "AM-2026-0042"])][:118]
df["ID Cliente"] = df["ID Cliente"].astype(object)
df.loc[pool_sc[:60], "ID Cliente"] = np.nan
df.loc[pool_sc[60:98], "ID Cliente"] = ""
df.loc[pool_sc[98:118], "ID Cliente"] = "SIN-ID"
df.loc[pool_sc, "Nombre Cliente"] = np.nan

# P7 · Descuento NaN (no registrado)
pool_d = rng.choice(np.setdiff1d(np.arange(n), pool_sc), 210, replace=False)
df.loc[pool_d, "Descuento"] = np.nan

# P9 · Utilidad centinela -9999
pool_u = rng.choice(np.arange(n), 14, replace=False)
df.loc[pool_u, "Utilidad"] = -9999

# P10 · Provincia nula
pool_p = rng.choice(np.arange(n), 31, replace=False)
df.loc[pool_p, "Provincia"] = np.nan

# P8 · Cantidad negativa (devoluciones)
pool_q = rng.choice(np.setdiff1d(np.arange(n), df.index[df["ID Pedido"] == "AM-2026-0042"]), 9, replace=False)
df.loc[pool_q, "Cantidad"] = -df.loc[pool_q, "Cantidad"].abs()

# P6 · Ciudad inconsistente
qui = df.index[df["Ciudad"] == "Quito"].to_numpy()
v1 = rng.choice(qui, 40, replace=False)
df.loc[v1[:18], "Ciudad"] = "QUITO"
df.loc[v1[18:30], "Ciudad"] = "quito"
df.loc[v1[30:40], "Ciudad"] = " Quito"
sd = df.index[df["Ciudad"] == "Santo Domingo"].to_numpy()
v2 = rng.choice(sd, 14, replace=False)
df.loc[v2, "Ciudad"] = "Sto. Domingo"

# P4 · envío antes del pedido (6 filas)
pool_f = rng.choice(np.setdiff1d(np.arange(n), df.index[df["ID Pedido"] == "AM-2026-0042"]), 6, replace=False)
df.loc[pool_f, "Fecha Envío"] = df.loc[pool_f, "Fecha Pedido"] - pd.Timedelta(days=3)

# P3 · fechas a texto, 35 en dd/mm/yyyy
fp = df["Fecha Pedido"].dt.strftime("%Y-%m-%d")
fe = df["Fecha Envío"].dt.strftime("%Y-%m-%d")
pool_t = rng.choice(np.arange(n), 35, replace=False)
fp.iloc[pool_t] = df["Fecha Pedido"].iloc[pool_t].dt.strftime("%d/%m/%Y")
fe.iloc[pool_t] = df["Fecha Envío"].iloc[pool_t].dt.strftime("%d/%m/%Y")
df["Fecha Pedido"], df["Fecha Envío"] = fp, fe

# P5 · Ventas como texto "$1.234,56" en 42 filas
df["Ventas"] = df["Ventas"].astype(object)
pool_v = rng.choice(np.setdiff1d(np.arange(n), df.index[df["ID Pedido"] == "AM-2026-0042"]), 42, replace=False)
for i in pool_v:
    v = float(df.at[i, "Ventas"])
    df.at[i, "Ventas"] = "$" + f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# P2 · duplicados exactos: 24 filas repetidas al final
dup = df.iloc[rng.choice(np.arange(n), 24, replace=False)].copy()
df = pd.concat([df, dup], ignore_index=True)
df = df.sample(frac=1, random_state=7).reset_index(drop=True)
df.insert(0, "ID Fila", np.arange(1, len(df) + 1))

# ── Guardar y medir clave ────────────────────────────────────────────────
out = AQUI / "andina_market.csv"
df.to_csv(out, index=False, encoding="utf-8-sig")

sc_nan = int(df["ID Cliente"].isna().sum())
sc_vacio = int((df["ID Cliente"] == "").sum())
sc_sinid = int((df["ID Cliente"] == "SIN-ID").sum())
sc_total = sc_nan + sc_vacio + sc_sinid
mask_sc = df["ID Cliente"].isna() | df["ID Cliente"].isin(["", "SIN-ID"])
por_region = (mask_sc.groupby(df["Región"]).mean() * 100).round(1).to_dict()
ventas_num = pd.to_numeric(df["Ventas"], errors="coerce")
ventas_texto = int(ventas_num.isna().sum())
suma_real = float(ventas_num.sum() + sum(float(str(v)[1:].replace(".", "").replace(",", "."))
                                         for v in df.loc[ventas_num.isna(), "Ventas"]))
clave = {
    "filas": int(len(df)), "columnas": int(df.shape[1]),
    "duplicados_exactos": int(df.drop(columns=["ID Fila"]).duplicated().sum()),
    "sin_cliente": {"nan": sc_nan, "vacio": sc_vacio, "sin_id": sc_sinid, "total": sc_total,
                    "pct": round(100 * sc_total / len(df), 1), "por_region_pct": por_region},
    "descuento_nan": int(df["Descuento"].isna().sum()),
    "descuento_cero": int((df["Descuento"] == 0).sum()),
    "utilidad_centinela": int((df["Utilidad"] == -9999).sum()),
    "provincia_nan": int(df["Provincia"].isna().sum()),
    "cantidad_negativa": int((df["Cantidad"] < 0).sum()),
    "ciudad_variantes_quito": sorted(set(c for c in df["Ciudad"] if c.strip().lower() == "quito")),
    "ciudad_sto_domingo": int((df["Ciudad"] == "Sto. Domingo").sum()),
    "fechas_ddmm": int(df["Fecha Pedido"].str.contains("/").sum()),
    "envio_antes_pedido": 6,
    "ventas_texto": ventas_texto,
    "pedido_ejemplo": {"id": "AM-2026-0042", "lineas": 4, "total": 187.40,
                       "suma_total_pedido_mal": round(187.40 * 4, 2)},
    "suma_ventas_real": round(suma_real, 2),
    "suma_total_pedido_doble": round(float(df["Total Pedido"].sum()), 2),
}
(AQUI / "clave.json").write_text(json.dumps(clave, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(clave, indent=2, ensure_ascii=False))
