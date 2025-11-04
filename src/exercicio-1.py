def atualizar_estoque(estoque, livro, quantidade):
    if livro in estoque:
        novo = estoque[livro] + quantidade
    else:
        novo = quantidade

    if novo <= 0:
        estoque.pop(livro, None)
    else:
        estoque[livro] = novo

    print("Estoque atual:", estoque)
    return estoque


estoque = {
    "Python Crash Course": 4,
    "Clean Code": 2,
    "Automate the Boring Stuff": 0
}

atualizar_estoque(estoque, "Clean Code", 3)
atualizar_estoque(estoque, "Fluent Python", 5)
atualizar_estoque(estoque, "Automate the Boring Stuff", 0)
