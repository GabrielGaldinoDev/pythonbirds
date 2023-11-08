class Pessoa:
    olhos = 2
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
    Gabriel.sobrenome = 'Galdino'
    del Gabriel.filhos
    valentina.olhos=1
    del valentina.olhos
    print(Gabriel.__dict__)
    print(valentina.__dict__)
    Pessoa.olhos=3
    print(Pessoa.olhos)
    print(Gabriel.olhos)
    print(valentina.olhos)