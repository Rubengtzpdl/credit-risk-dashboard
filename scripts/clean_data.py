import pandas as pd

# Cargar datos
df = pd.read_excel("data/raw/cartera_credito.xlsx")

# Calcular columnas nuevas
df["tasa_morosidad_%"] = (df["cartera_vencida_mdp"] / df["cartera_vigente_mdp"] * 100).round(2)
df["credito_promedio_mdp"] = (df["cartera_vigente_mdp"] / df["num_creditos"]).round(4)

# Clasificar zonas de riesgo
def clasificar_riesgo(morosidad):
    if morosidad < 3.0:
        return "Riesgo Bajo"
    elif morosidad < 4.5:
        return "Riesgo Medio"
    else:
        return "Riesgo Alto"

df["zona_riesgo"] = df["indice_morosidad"].apply(clasificar_riesgo)

# Guardar datos procesados
df.to_excel("data/processed/cartera_limpia.xlsx", index=False)

print("✅ Datos procesados correctamente")
print(df[["entidad", "indice_morosidad", "zona_riesgo"]])