import time
from statistics import mean

sensores_lista = [("S1", 34), ("S2", 36), ("S3", 37), ("S4", 38)]
sensores_dict = {"S1": 34, "S2": 36, "S3": 37, "S4": 38}

N = 10000
tempos_lista = []
tempos_dict = []

for _ in range(N):

    t0 = time.perf_counter()
    for k, v in sensores_lista:
        if k == "S3":
            _ = v
            break
    t1 = time.perf_counter()
    tempos_lista.append(t1 - t0)

    t0 = time.perf_counter()
    _ = sensores_dict["S3"]
    t1 = time.perf_counter()
    tempos_dict.append(t1 - t0)

print("# Relatório de Comparação de Desempenho")
print("Execuções:", N)
print(f"Tempo médio (lista): {mean(tempos_lista):.9f} segundos")
print(f"Tempo médio (dicionário): {mean(tempos_dict):.9f} segundos")
