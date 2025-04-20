# Módulo 4: Visualización de Datos

La visualización es esencial para comprender patrones, tendencias y anomalías en los datos. Este módulo se centra en el uso de librerías como Matplotlib (a menudo junto con Pandas) para crear diversos tipos de gráficos.

## Proyectos del Módulo

* **Visualización Básica con Matplotlib:** (`visualizacion.py`) - Creación de gráficos simples (líneas, barras, dispersión, histogramas) a partir de datos cargados con Pandas.
    * *Documentación detallada:* `README.md` *(a crear o renombrar/fusionar si ya existe uno genérico para este proyecto)*

## Conceptos Clave del Módulo

* Importar `matplotlib.pyplot` como `plt`.
* Crear figuras y ejes (subplots).
* Generar gráficos básicos:
    * `plt.plot()` (gráficos de líneas)
    * `plt.scatter()` (gráficos de dispersión)
    * `plt.bar()` / `plt.barh()` (gráficos de barras)
    * `plt.hist()` (histogramas)
* Personalización de gráficos:
    * Títulos (`plt.title()`)
    * Etiquetas de ejes (`plt.xlabel()`, `plt.ylabel()`)
    * Leyendas (`plt.legend()`)
* Mostrar gráficos (`plt.show()`).
* Integración con Pandas para graficar directamente desde DataFrames (`df.plot()`).

---

[Volver al Índice Principal](../README.md)