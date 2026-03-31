import pandas as pd

df = pd.read_excel("data/raw/cartera_credito.xlsx", engine="openpyxl")
print(df.shape)
print(df.head())