#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepara superstore_2026 a partir del Superstore clásico (Kaggle, 2014–2017).

Qué hace, en orden:
1. Desplaza TODAS las fechas un múltiplo exacto de 7 días, de modo que el último
   pedido caiga el sábado anterior al inicio de la semana 3 del curso
   (29-ago-2026). Al ser múltiplo de 7 se conservan los días de semana y, como
   ningún valor cambia, se conservan exactamente los estadísticos del dataset
   original. No hay pedidos con fecha futura; algunos envíos recientes quedan
   "en tránsito", como en la vida real.
2. Reescribe el año dentro de `pedido_id` (CA-2017-152156 → CA-2026-152156)
   para que coincida con el año de la fecha desplazada.
3. Traduce columnas y valores categóricos al español. Los nombres de producto,
   clientes y lugares quedan en su idioma original: Superstore es una cadena
   estadounidense y así llegan los datos de verdad.
4. Escribe superstore_2026.csv y superstore_2026.xlsx, e imprime las
   comprobaciones didácticas: si alguna de las trampas de la sesión 5 deja de
   estar en los datos, este script avisa.

Uso:  python3 preparar_superstore.py [ruta_al_superstore.xlsx]
"""
import sys
from pathlib import Path

import pandas as pd

AQUI = Path(__file__).resolve().parent
ORIGEN = Path(sys.argv[1]) if len(sys.argv) > 1 else AQUI / "superstore_original.xlsx"
FECHA_TOPE = pd.Timestamp("2026-08-29")  # sábado previo a la sesión 5 (lun 31-ago-2026)

COLUMNAS = {
    "Order ID": "pedido_id", "Order Date": "fecha_pedido", "Ship Date": "fecha_envio",
    "Ship Mode": "modo_envio", "Customer ID": "cliente_id", "Customer Name": "cliente",
    "Segment": "segmento", "Country": "pais", "City": "ciudad", "State": "estado",
    "Postal Code": "codigo_postal", "Region": "region", "Product ID": "producto_id",
    "Category": "categoria", "Sub-Category": "subcategoria", "Product Name": "producto",
    "Sales": "venta", "Quantity": "cantidad", "Discount": "descuento", "Profit": "utilidad",
}
VALORES = {
    "modo_envio": {"Standard Class": "Estándar", "Second Class": "Segunda clase",
                   "First Class": "Primera clase", "Same Day": "Mismo día"},
    "segmento": {"Consumer": "Consumidor", "Corporate": "Corporativo",
                 "Home Office": "Oficina en casa"},
    "pais": {"United States": "Estados Unidos"},
    "region": {"West": "Oeste", "East": "Este", "Central": "Centro", "South": "Sur"},
    "categoria": {"Furniture": "Muebles", "Office Supplies": "Suministros de Oficina",
                  "Technology": "Tecnología"},
    "subcategoria": {"Bookcases": "Libreros", "Chairs": "Sillas", "Tables": "Mesas",
                     "Furnishings": "Decoración", "Phones": "Teléfonos",
                     "Copiers": "Copiadoras", "Machines": "Máquinas",
                     "Accessories": "Accesorios", "Appliances": "Electrodomésticos",
                     "Art": "Arte", "Binders": "Carpetas", "Envelopes": "Sobres",
                     "Fasteners": "Sujetadores", "Labels": "Etiquetas", "Paper": "Papel",
                     "Storage": "Almacenamiento", "Supplies": "Insumos"},
}


def main() -> None:
    df = pd.read_excel(ORIGEN)

    # 1 · Desplazamiento de fechas (múltiplo de 7 días → se conservan los días de semana)
    dias = (FECHA_TOPE - df["Order Date"].max()).days
    dias -= dias % 7
    for col in ("Order Date", "Ship Date"):
        df[col] = df[col] + pd.Timedelta(days=dias)
    assert df["Order Date"].max() <= FECHA_TOPE

    # 2 · pedido_id con el año nuevo (CA-2017-152156 → CA-2026-152156)
    partes = df["Order ID"].str.split("-", expand=True)  # prefijo, año, número
    df["Order ID"] = (partes[0] + "-" + df["Order Date"].dt.year.astype(str)
                      + "-" + partes[2])
    # un pedido = un id; un id = un pedido (no puede haber colisiones tras el cambio)
    assert df.groupby("Order ID")["Order Date"].nunique().max() == 1
    assert df["Order ID"].nunique() == 5009

    # 3 · Traducción
    df = df.drop(columns=["Row ID"]).rename(columns=COLUMNAS)
    for col, mapa in VALORES.items():
        df[col] = df[col].map(mapa)
        assert not df[col].isna().any(), f"valor sin traducir en {col}"
    df.insert(0, "linea_id", range(1, len(df) + 1))

    # 4 · Salida
    df.to_csv(AQUI / "superstore_2026.csv", index=False)
    df.to_excel(AQUI / "superstore_2026.xlsx", index=False)

    # Comprobaciones didácticas de la sesión 5
    ped = df.groupby("pedido_id")["venta"].sum()
    prom, med = ped.mean(), ped.median()
    bajo = (ped < prom).mean() * 100
    print(f"{len(df)} líneas · {len(ped)} pedidos · "
          f"{df['fecha_pedido'].min():%Y-%m-%d} → {df['fecha_pedido'].max():%Y-%m-%d}"
          f" (desplazadas {dias} días)")
    print(f"Trampa 1 · pedido típico: media {prom:.2f} vs mediana {med:.2f} · "
          f"{bajo:.1f}% de pedidos bajo la media")
    assert prom / med > 2.5 and bajo > 65, "la cola larga del ticket se perdió"

    g = df.groupby("categoria")["utilidad"].agg(["mean", "median"]).round(2)
    print("Trampa 2 · utilidad por línea:", g.to_dict("index"))
    assert (g.loc["Suministros de Oficina", "mean"] > 2 * g.loc["Muebles", "mean"]
            and g.loc["Muebles", "median"] > g.loc["Suministros de Oficina", "median"]), \
        "el vuelco media/mediana entre categorías se perdió"

    lib = df.loc[df["subcategoria"] == "Libreros", "utilidad"]
    print(f"Trampa 3 · Libreros: media {lib.mean():.2f} vs mediana {lib.median():.2f} "
          f"· total {lib.sum():,.0f}")
    assert lib.mean() < 0 < lib.median(), "la trampa inversa de Libreros se perdió"

    desc = df.loc[df["descuento"] > 0, "utilidad"]
    print(f"Bonus · líneas con descuento: media {desc.mean():.2f} "
          f"vs mediana {desc.median():.2f}")
    assert desc.mean() < 0 < desc.median(), "la bimodalidad del descuento se perdió"
    print("Comprobaciones didácticas ✓")


if __name__ == "__main__":
    main()
