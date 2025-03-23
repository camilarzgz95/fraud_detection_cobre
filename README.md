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
├── requirements.txt
└── README.md
```

## 🚀 Cómo usar

1. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

2. Ejecuta manualmente el notebook principal:

```bash
notebooks/fraud_pipeline_completo_umbral.ipynb
```

Este notebook genera los siguientes archivos en `data/generado/`:
- `tabla_1_inicial.csv`
- `tabla_2_validaciones.csv`
- `tabla_3_reglas.csv`
- `tabla_output_clientes.csv`

3. Luego, ejecuta el notebook de resumen:

```bash
notebooks/fraud_pipeline_resumen.ipynb
```

Este notebook reconstruye `df_merged` desde las tablas generadas e incluye visualizaciones, insights y explicación de los factores de riesgo.

---

## 📥 Archivos originales

Los archivos originales no están incluidos por su tamaño.

Por favor, descárgalos manualmente desde [Kaggle IEEE Fraud Detection](https://www.kaggle.com/competitions/ieee-fraud-detection/data)  
y colócalos en `data/original/` antes de ejecutar el pipeline.