import json

produtos = {
    "Smartphone": {"preco": 2500, "estoque": 12},
    "Notebook": {"preco": 4800, "estoque": 5},
    "Fone Bluetooth": {"preco": 300, "estoque": 25}
}

with open("produtos.json", "w", encoding="utf-8") as f:
    json.dump(produtos, f, ensure_ascii=False, indent=2)

with open("produtos.json", encoding="utf-8") as f:
    dados = json.load(f)

print(type(dados))  
print("Produtos carregados:", list(dados.keys()))
