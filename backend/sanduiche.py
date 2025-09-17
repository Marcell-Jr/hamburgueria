class Lanche:
    def __init__(self,nome,preco,ingredientes):
        self.nome = nome
        self.preco = preco 
        self.ingredientes = ingredientes

    def exbiriLanche(self):
        """
        Exibe os dados do lanche cadastrado (nome, preco e ingredientes)
        """
        print(f"Sanduíche:{self.nome}; Preço:{self.preco};ingredientes:{self.ingredientes}")