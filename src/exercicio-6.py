import pandas as pd
from datetime import date

medicamentos = {"Aspirina":"2024-11-01","Dipirona":"2026-03-10","Paracetamol":"2023-12-01"}

df = pd.Series(medicamentos).reset_index()

df.columns = ['produto','validade']

df['validade'] = pd.to_datetime(df["validade"]).dt.date

data_hoje = date.today()

valido = df[df["validade"] >= data_hoje]

removidos = len(df) - len(valido)

print("Removidos:", removidos)
print(valido.set_index('produto')['validade'].to_dict())
