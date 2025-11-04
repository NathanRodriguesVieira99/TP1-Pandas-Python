config = {
    "servidor": "192.168.0.10",
    "porta": 8080,
    "modo": "produção"
}

# escreve
with open("config.txt", "w", encoding="utf-8") as f:
    for k, v in config.items():
        f.write(f"{k} = {v}\n")

# ler e imprime
with open("config.txt", encoding="utf-8") as f:
    for linha in f:
        chave, valor = linha.strip().split("=", 1)
        print(f"{chave.strip().capitalize()}: {valor.strip()}")
