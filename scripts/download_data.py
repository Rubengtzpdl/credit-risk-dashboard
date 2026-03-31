import pandas as pd
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://www.cnbv.gob.mx/SECTORES-SUPERVISADOS/BANCA-MULTIPLE/Boletines-Estadisticos/BM%20Cartera%20de%20Credito%20Vigente%20y%20Vencida.xlsx"

print("Descargando datos de CNBV...")

try:
    response = requests.get(url, timeout=30, verify=False)
    with open("data/raw/cartera_credito.xlsx", "wb") as f:
        f.write(response.content)
    print("✅ Datos descargados correctamente")
except Exception as e:
    print(f"❌ Error: {e}")