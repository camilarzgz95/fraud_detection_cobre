import pandas as pd
import os

print("📦 Cargando archivos generados...")

base_path = os.path.join("data", "generado")
tabla_1 = pd.read_csv(os.path.join(base_path, "tabla_1_inicial.csv"))
tabla_2 = pd.read_csv(os.path.join(base_path, "tabla_2_validaciones.csv"))
tabla_3 = pd.read_csv(os.path.join(base_path, "tabla_3_reglas.csv"))

# Reconstruir df_merged
df_merged = tabla_1.merge(tabla_2, on=['TransactionID', 'ClientID'])
df_merged = df_merged.merge(tabla_3, on=['TransactionID', 'ClientID'])

print("✅ Dataset reconstruido con", df_merged.shape[0], "transacciones.")

# Mostrar resumen simple
print("\n🔍 Transacciones fraudulentas detectadas:", df_merged['FlagFraude'].sum())
print("🎯 Promedio ScoreFraude (fraude):", round(df_merged[df_merged['FlagFraude'] == 1]['ScoreFraude'].mean(), 2))
print("💳 Tarjetas más comunes en fraude:")
print(df_merged[df_merged['FlagFraude'] == 1]['card4'].value_counts().head(3))

# Guardar una versión reducida si se desea
df_merged.head(100).to_csv("df_merged_preview.csv", index=False)
print("\n📝 Archivo 'df_merged_preview.csv' generado con las primeras 100 filas.")