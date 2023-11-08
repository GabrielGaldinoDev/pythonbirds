class Pessoa:
    def __init__(self, *filhos, nome=None, idade=26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    valentina = Pessoa(nome='valentina')
    Gabriel = Pessoa(valentina, nome='gabriel')
    print(Pessoa.cumprimentar(Gabriel))
    print(id(Gabriel))
    print(Gabriel.cumprimentar())
    print(Gabriel.nome)
    print(Gabriel.idade)
    for filho in Gabriel.filhos:
        print(filho.nome)