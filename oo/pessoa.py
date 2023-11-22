class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'
    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'
class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    valentina = Mutante(nome='valentina')
    Gabriel = Homem(valentina, nome='gabriel')
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
    print(Pessoa.olhos)
    print(Gabriel.olhos)
    print(valentina.olhos)
    print((Pessoa.metodo_estatico(),Gabriel.metodo_estatico()))
    print((Pessoa.nome_e_atributo_de_classe(),Gabriel.nome_e_atributo_de_classe()))
    print(valentina.olhos)
    print(Gabriel.cumprimentar())
    print(valentina.cumprimentar())