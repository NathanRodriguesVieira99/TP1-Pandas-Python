from pathlib import Path
import pandas as pd
import re

path = Path(__file__).resolve().parent / "relatorio.txt"

texto = path.read_text(encoding="utf-8").lower()
palavras = re.findall(r"\w+", texto, flags=re.UNICODE)

s = pd.Series(palavras)
top3 = s.value_counts().head(3)
print("Top 3 palavras mais frequentes:")
for palavra, cont in top3.items():
	print(f"{palavra}: {cont}")
