import pandas as pd


emails = ["ana@empresa.com","bruno@empresa.com","ana@empresa.com","carla@empresa.com","bruno@empresa.com","daniel@empresa.com"]

s = pd.Series(emails)

unicos = s.drop_duplicates().sort_values().tolist()

print("Duplicatas removidas:", len(emails) - len(unicos))
print(unicos)
