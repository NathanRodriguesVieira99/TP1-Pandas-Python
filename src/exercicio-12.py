import json

campanha_1 = ["Ana", "Bruno", "Carla"]
campanha_2 = ["Bruno", "Daniel", "Eduardo"]
campanha_3 = ["Ana", "Fernanda", "Gustavo"]

base_unica = set(campanha_1) | set(campanha_2) | set(campanha_3)
dados = {"total": len(base_unica), "nomes": list(base_unica)}

with open("clientes_unicos.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)

with open("clientes_unicos.json", encoding="utf-8") as f:
    carregado = json.load(f)

print("Total carregado:", carregado["total"])
