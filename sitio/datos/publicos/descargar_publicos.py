#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Descarga los datasets públicos del curso, uno por industria.

Los archivos ya vienen incluidos en el repositorio: este script existe para
poder regenerarlos o actualizarlos. Dos vienen del propio curso anterior
(pizza_ventas desde el adjunto de D2L y credit.csv) y el resto de fuentes
públicas estables (TidyTuesday, FiveThirtyEight, IBM, mirrors de GitHub).

Uso:  python3 descargar_publicos.py
"""
import os
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))

URLS = {
    # música · TidyTuesday 2020-01-21
    "spotify_canciones.csv": "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv",
    # streaming · TidyTuesday 2021-04-20
    "netflix_titulos.csv": "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-04-20/netflix_titles.csv",
    # cine y género · FiveThirtyEight
    "peliculas_bechdel.csv": "https://raw.githubusercontent.com/fivethirtyeight/data/master/bechdel/movies.csv",
    # videojuegos · TidyTuesday 2021-03-16 (jugadores mensuales en Steam)
    "videojuegos_steam.csv": "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-16/games.csv",
    # retail · Sample Superstore (mirror)
    "superstore.csv": "https://raw.githubusercontent.com/leonism/sample-superstore/master/data/superstore.csv",
    # telecomunicaciones · IBM Telco Customer Churn (el caso Telco de 202410)
    "telco_churn.csv": "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv",
    # recursos humanos · IBM HR Attrition (el caso Abandono Laboral de 202520)
    "rrhh_abandono.csv": "https://raw.githubusercontent.com/IBM/employee-attrition-aif360/master/data/emp_attrition.csv",
    # autos y ambiente · mpg (la práctica de emisiones CO2 de 202520)
    "co2_vehiculos.csv": "https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv",
    # café y agro · TidyTuesday 2020-07-07
    "cafe_calidad.csv": "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-07/coffee_ratings.csv",
    # aviación · nycflights13 (se muestrea a 60 000 filas al final)
    "vuelos_nyc.csv": "https://raw.githubusercontent.com/byuidatascience/data4python4ds/master/data-raw/flights/flights.csv",
}

PIZZA_XLSX = os.path.join(
    AQUI, "..", "..", "..", "Material Actual", "Actividades Organizadas",
    "02_Primer_Contacto_con_Datos_y_EDA",
    "2025_Taller_02_Ejercicio_Analisis_Individual_Pizza_Sales",
    "adjuntos", "pizza_sales.xlsx")
CREDIT_CSV = os.path.join(
    AQUI, "..", "..", "..", "Material Actual", "Actividades Organizadas",
    "03_Estadistica_Descriptiva",
    "2024_Python_Estadistica_descriptiva_con_Pandas", "adjuntos", "Credit.csv")


def main():
    for nombre, url in URLS.items():
        destino = os.path.join(AQUI, nombre)
        req = urllib.request.Request(url, headers={"User-Agent": "curso-usfq/1.0"})
        with urllib.request.urlopen(req, timeout=90) as r, open(destino, "wb") as f:
            f.write(r.read())
        print(f"OK {nombre} ({os.path.getsize(destino) // 1024} KB)")

    import pandas as pd

    # pizza y credit vienen del material heredado del propio curso
    if os.path.exists(PIZZA_XLSX):
        pd.read_excel(PIZZA_XLSX).to_csv(os.path.join(AQUI, "pizza_ventas.csv"), index=False)
        print("OK pizza_ventas.csv (desde el adjunto de D2L)")
    if os.path.exists(CREDIT_CSV):
        import shutil
        shutil.copy(CREDIT_CSV, os.path.join(AQUI, "credit.csv"))
        print("OK credit.csv (desde el adjunto de D2L)")

    # vuelos: el original pesa 30 MB; se muestrea estratificado por mes
    ruta = os.path.join(AQUI, "vuelos_nyc.csv")
    v = pd.read_csv(ruta)
    if len(v) > 60000:
        m = (v.groupby("month", group_keys=False)
              .apply(lambda g: g.sample(n=min(5000, len(g)), random_state=42),
                     include_groups=True))
        m.to_csv(ruta, index=False)
        print(f"OK vuelos_nyc.csv muestreado a {len(m):,} filas")


if __name__ == "__main__":
    main()
