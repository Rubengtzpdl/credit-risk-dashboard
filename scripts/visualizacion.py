import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data/processed/cartera_limpia.xlsx")


colores = {
    "Riesgo Bajo": "verde",
    "Riesgo Medio": "naranja",
    "Riesgo Alto": "rojo"
}

df_sorted = df.sort_values("indice_morosidad", ascending=True)
colores_barras = [colores[r] for r in df_sorted["zona_riesgo"]]

plt.figure(figsize=(12, 6))
plt.barh(df_sorted["entidad"], df_sorted["indice_morosidad"], color=colores_barras)
plt.xlabel("Índice de Morosidad (%)")
plt.title("Índice de Morosidad por Entidad Federativa")
plt.axvline(x=3.0, color="gray", linestyle="--", label="Umbral Riesgo Medio")
plt.axvline(x=4.5, color="red", linestyle="--", label="Umbral Riesgo Alto")
plt.legend()
plt.tight_layout()
plt.savefig("reports/morosidad_por_estado.png")
plt.show()
print("Gráfica guardada en reports/")
