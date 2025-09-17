class Lanche:
    def __init__(self, nome, ingredientes, preco):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes

lanche1 = Lanche('X Tudo', 'pao, alface, tomate, milho, queijo, presunto, hamburguer, ovo', 30.00)
lanche2 = Lanche('X Salada', 'pao, alface, tomate, milho, queijo, hamburguer', 20.00)

print(lanche1.nome)
print(lanche1.ingredientes)
print(lanche1.preco)

print(lanche2.nome)
print(lanche2.ingredientes)
print(lanche2.preco)

