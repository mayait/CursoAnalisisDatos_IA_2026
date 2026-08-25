# Caso 2 · Análisis Comparativo del Sistema Bancario Ecuatoriano
### Seminario Análisis Exploratorio de Datos 
**Riesgo de complejidad:** 🟡 Medio · **Técnica principal:** EDA + Rankings · **Dominio:** Finanzas / Ecuador

---

## 🏢 Antecedentes

La Superintendencia de Bancos del Ecuador publica mensualmente un boletín estadístico con la situación financiera de los **24 bancos privados** del país. Estos archivos Excel tienen un formato institucional complejo: encabezados multinivel, celdas fusionadas y los indicadores organizados con los bancos en las columnas en lugar de las filas — el opuesto del formato analítico estándar.

Los nombres de las entidades bancarias pueden variar entre hojas (`"PICHINCHA"`, `"BP PICHINCHA"`) lo que exige estandarización antes de hacer joins. Un analista financiero o del Banco Central necesita una herramienta que transforme esos datos oficiales en un sistema de comparación interactivo de uso inmediato.

---

## 🎯 Objetivo

Transformar el boletín estadístico oficial de la Superintendencia de Bancos en un sistema de inteligencia financiera que permita **comparar, rankear y analizar** el desempeño de las 24 instituciones por sus principales indicadores: tamaño (activos), rentabilidad (ROE), calidad de cartera (tasa de morosidad) y solvencia.

---

## 📚 Actividades para el estudiante

**Resultado de aprendizaje:** el estudiante transforma datos públicos de formato no estándar en un sistema analítico de inteligencia bancaria, aplicando técnicas de reestructuración de datos.

### Fase 1 – Comprensión del dominio
Investigar los cuatro indicadores financieros clave del sector bancario ecuatoriano: activos totales, ROE, tasa de morosidad e índice de solvencia. Explorar el portal de la Superintendencia de Bancos e identificar el boletín estadístico más reciente. Formular hipótesis sobre cuáles instituciones lideran en cada indicador.

### Fase 2 – Preparación y exploración de datos
Descargar el boletín y examinar su estructura. Identificar los desafíos de las hojas BALANCE, COMPOS CART e INDICADORES: encabezados multinivel, celdas fusionadas, bancos en columnas. Transformar cada hoja de **formato ancho a formato largo** (una fila por banco). Estandarizar los nombres de las instituciones para asegurar joins correctos entre hojas. Construir la tabla maestra consolidada con todos los KPIs por banco. Calcular el índice de solvencia como indicador adicional derivado.

### Fase 3 – Análisis comparativo
Calcular estadísticas descriptivas del sistema en su conjunto. Identificar outliers y analizar su significado regulatorio. Comparar el desempeño relativo de cada banco respecto al promedio del sistema. Generar rankings ordenados por cada KPI.

### Fase 4 – Producto analítico

**Pipeline técnico:**
- Navegar a `https://www.superbancos.gob.ec/estadisticas/` y descargar el boletín más reciente
- Leer cada hoja con parámetros para manejar encabezados multinivel (`skiprows`, `header`)
- Aplicar `pandas.melt` para transformar de "bancos en columnas" a formato tidy
- Estandarizar nombres con `str.strip().str.upper()` antes de los joins
- Exportar la tabla maestra limpia a formato Parquet para el dashboard

**API (FastAPI):**
- `GET /financials/bank?name=Pichincha` — todos los KPIs de un banco específico
- `GET /financials/rank?kpi=assets` — ranking de los 24 bancos por indicador seleccionado

**Dashboard (Streamlit):**
1. Tabla comparativa interactiva y ordenable por cualquier KPI con todos los bancos simultáneos
2. Gráfico de barras horizontales del top 10 por el KPI seleccionado
3. Tarjeta de perfil del banco elegido con sus indicadores vs. el promedio del sistema

### Fase 5 – Interpretación y comunicación
¿Qué banco lidera en rentabilidad y cuál en solidez patrimonial? ¿Existen instituciones con señales de riesgo en su cartera? ¿Qué implicaciones tendría esto para un regulador financiero o para un depositante común?

---

## 🗂️ Dataset y recursos

| Recurso | Enlace |
|---|---|
| **Dataset principal** | [Portal de Estadísticas — Superintendencia de Bancos Ecuador](https://www.superbancos.gob.ec/estadisticas/) |

**Lecturas recomendadas:**
- Indicadores financieros del sector bancario: activos, ROE, morosidad, solvencia
- Lectura avanzada de archivos Excel con múltiples hojas y encabezados complejos
- Reestructuración de datos: transformación de formato ancho a formato largo (melt)
- Estandarización y limpieza de nombres para joins entre tablas


---

## 📋 Rúbrica de evaluación

| Entregable | Semana | Peso | Criterios clave |
|---|---|---|---|
| Definición del problema | 1 | 10 % | Claridad de la pregunta de negocio, historias de usuario, ficha del dataset |
| Pipeline de datos | 2 | 20 % | Reproducibilidad, manejo del reto específico, validaciones documentadas |
| EDA + primer modelo | 3 | 25 % | Profundidad del análisis, rigor estadístico, pertinencia del modelo y métricas |
| Producto analítico completo | 4 | 30 % | Comparación de ≥ 2 modelos, API y dashboard funcionales, documentación |
| Defensa oral y trabajo en equipo | 4 | 15 % | Dominio técnico, claridad, manejo de preguntas, colaboración |

> **Modalidad:** grupos de 3 estudiantes · **Entrega final:** sesión final del seminario
