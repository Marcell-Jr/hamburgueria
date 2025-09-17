from sanduiche import Lanche
from cardapio import Cardapio

resposta = 's'

c = Cardapio()
while resposta == 's':

    ingredientes = []
    nome = input("Nome do sanduíche:")
    preco=float(input("Preço do sanduíche:  "))
    qtdeIngredientes = int(input("Escreve quantos ingredientes você quer adicionar:"))
    for i in range(qtdeIngredientes):
        ingrediente = input(f"Informe o ingrediente {i+1}:")
        ingredientes.append(ingrediente)

# Criando o objeto da classe Lanche dentro do Laço
        l = Lanche(nome,preco,ingredientes)

# Adicionando o lanche "l" ao cardapio "c"
c.adicionarItem(l)
resposta = input("deseja adicionar outro item ao cardápio (s/n)")

# FIM DO LAÇO WHILE
c.exibirCardapio()
