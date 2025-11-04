clientes_A = {"Ana", "Bruno", "Carla", "Daniel"}
clientes_B = {"Bruno", "Carla", "Eduardo", "Fernanda"}

intersecao = clientes_A & clientes_B
diferenca = clientes_A - clientes_B
uniao = clientes_A | clientes_B
total_unicos = len(uniao)

print("Interseção (comuns):", intersecao)
print("Diferença (A - B):", diferenca)
print("União (todos):", uniao)
print("Total de clientes únicos:", total_unicos)
