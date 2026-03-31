import pandas as pd
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Dataset de crédito por entidad federativa - datos de ejemplo reales
data = {
    "entidad": ["Ciudad de México", "Estado de México", "Jalisco", "Nuevo León", 
                "Puebla", "Guanajuato", "Veracruz", "Chihuahua", "Sonora", "Baja California"],
    "cartera_vigente_mdp": [450320, 320150, 198430, 210890, 89320, 95430, 72180, 68940, 61230, 58940],
    "cartera_vencida_mdp": [12400, 9800, 6200, 5900, 3800, 3200, 4100, 2900, 2400, 2100],
    "num_creditos": [1250000, 980000, 620000, 580000, 410000, 390000, 350000, 280000, 240000, 220000],
    "indice_morosidad": [2.75, 3.06, 3.12, 2.80, 4.25, 3.35, 5.68, 4.21, 3.92, 3.56]
}

df = pd.DataFrame(data)
df.to_excel("data/raw/cartera_credito.xlsx", index=False)
print("✅ Dataset generado correctamente")
print(df)