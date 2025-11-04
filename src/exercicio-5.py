import pandas as pd

temperaturas = {"RJ":29.4,"SP":-99.0,"MG":27.2,"BA":31.1,"RS":-88.0}

s = pd.Series(temperaturas)
s_ok = s[s > -50]

print("Removidas:", len(s) - len(s_ok))
print("Restantes:", s_ok.to_dict())
