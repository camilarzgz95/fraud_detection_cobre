# 🛡️ Detección de Fraude Transaccional - Proyecto

Este repositorio contiene un sistema de detección de fraude basado en reglas, aplicado al dataset de IEEE-CIS.

## 📁 Estructura del Proyecto

```
fraud_project_github/
├── data/
│   ├── original/         <- Archivos originales cargados al inicio
│   └── generado/         <- Archivos generados por el notebook principal
├── notebooks/
│   ├── fraud_pipeline_completo_umbral.ipynb
│   └── fraud_pipeline_resumen.ipynb
├── run.py                <- Script para reconstruir df_merged y mostrar resumen
├── requirements.txt      <- Dependencias necesarias
└── README.md
```

## 🚀 Cómo usar

1. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

2. Ejecuta `notebooks/fraud_pipeline_completo_umbral.ipynb` para cargar y procesar los datos.
   - Este notebook genera los siguientes archivos en `data/generado/`:
     - `tabla_1_inicial.csv`
     - `tabla_2_validaciones.csv`
     - `tabla_3_reglas.csv`
     - `tabla_output_clientes.csv`

3. Puedes usar el script rápido para reconstruir el dataset y obtener un resumen:

```bash
python run.py
```

Esto cargará los datos y mostrará insights clave en consola.

4. Luego, ejecuta `notebooks/fraud_pipeline_resumen.ipynb`.
   - Este notebook lee los archivos generados.
   - Incluye visualizaciones, insights y explicación de los factores de riesgo.

## ✅ Requisitos

- Python 3.x
- pandas
- matplotlib
- seaborn
- jupyter (opcional para ejecutar notebooks)

Instalación rápida:

```bash
pip install -r requirements.txt
```