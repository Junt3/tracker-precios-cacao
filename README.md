# 📈 Tracker Automatizado de Precios del Cacao

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![yfinance](https://img.shields.io/badge/yfinance-Market_Data-green?style=for-the-badge)](https://pypi.org/project/yfinance/)

Un script de Python diseñado para automatizar la extracción y el registro histórico de los precios del cacao. El programa se conecta en tiempo real con el mercado internacional (ICE Nueva York) mediante la API de Yahoo Finance y permite el registro estructurado de los precios del mercado local ecuatoriano. 

Toda la información extraída se consolida dinámicamente en un conjunto de datos (CSV) que actúa como una base de datos histórica, lista para ser consumida por herramientas de Data Warehousing, canalizaciones ETL o dashboards de Business Intelligence.

## 🚀 Características Principales

*   **Integración de APIs Financieras:** Utiliza la librería `yfinance` para consultar el ticker `CC=F` (Futuros de Cacao) y extraer el último precio de cierre del mercado bursátil internacional.
*   **Procesamiento de Datos:** Emplea DataFrames de `pandas` para estructurar la información capturada junto con las marcas de tiempo (timestamps).
*   **Almacenamiento Persistente:** Genera y actualiza automáticamente un archivo CSV (`historial_precios_cacao.csv`). Si el archivo no existe, crea los encabezados; si ya existe, anexa los nuevos registros sin sobrescribir los datos previos.
*   **Gestión de Errores:** Incorpora manejo de excepciones para asegurar que fallos de conexión a la API no interrumpan la ejecución del programa.

## 🛠️ Tecnologías Utilizadas

*   **Lenguaje:** Python 3.x
*   **Análisis de Datos:** `pandas`
*   **Extracción de Datos Financieros:** `yfinance`

## ⚙️ Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/Junt3/tracker-precios-cacao.git](https://github.com/Junt3/tracker-precios-cacao.git)
    cd tracker-precios-cacao
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecutar el script:**
    ```bash
    python rastreador_cacao.py
    ```

4.  **Flujo del programa:**
    *   El script se conectará automáticamente a ICE Nueva York e imprimirá el precio actual por tonelada.
    *   Solicitará el ingreso del precio local actual por quintal.
    *   Guardará ambos valores junto con la fecha y hora exactas en el archivo de registro CSV.

---
*Este proyecto demuestra habilidades de extracción de datos (Data Ingestion) y automatización con Python, aplicadas al sector agroindustrial.*
