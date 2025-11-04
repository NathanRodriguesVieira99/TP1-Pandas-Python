registros = [
  ("Ana",[8,9,7]),
  ("Bruno",[5,6,5]),
  ("Carla",[10,9,10])
]

notas = {nome: lista for nome, lista in registros}

notas["Daniel"] = [7,7,8]

def media(lista):
      return sum(lista) / len(lista) if list else 0


removidos = []
for aluno in list(notas.keys()):
    if media(notas[aluno]) < 6:
        removidos.append(aluno)
        notas.pop(aluno)
        
print("Removidos:", removidos)
print("Notas finais:", notas)
