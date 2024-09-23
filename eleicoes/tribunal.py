from common import *

class Denuncia:
    __numero : int
    __denunciante : Pessoa
    __denunciado : Pessoa
    __juiz : Juiz
    __txt_denuncia : str
    __txt_sentenca : str

    def __init__(self, n: int, denunciante : Pessoa,
                 denunciado : Pessoa, txt_denuncia : str):
        self.__numero = n
        self.__denunciante = denunciante
        self.__denunciado = denunciado
        self.__txt_denuncia = txt_denuncia

    def julgar(self, j : Juiz, txt_sentenca : str):
        self.__juiz = j
        self.__txt_sentenca = txt_sentenca

    def __str__(self):
        if self.__txt_sentenca == None:
            info = f'Denuncia {self.__numero}. Sentenca não proferida'
        else:
            info = f'Denuncia {self.__numero}\n'
            info += f'Denunciante\n{self.__denunciante}\n'
            info += f'Assinatura: {self.__denunciante.assinatura_eletronica()}\n'
            info += f'Denunciado\n{self.__denunciado}\n'
            info += f'Assinatura: {self.__denunciado.assinatura_eletronica()}\n'
            info += f'Denuncia: {self.__txt_denuncia}\n'
            info += f'Sentença\n{self.__txt_sentenca}\n'
            info += f'Juiz\n{self.__juiz}\n'
            info += f'Assinatura: {self.__juiz.assinatura_eletronica()}'
        return info

if __name__ == "__main__":
    j1 = Juiz("Alex Morales", "12312", 123123, 4456)
    #p1 = Pessoa("Jose", 123123, 123123)
    c1 = Candidato("ADADADA", "223", "23123", 1)
    c2 = Candidato("xxxxxxx", "333", "444", 2)
    denun = Denuncia(1, c1, c2, "Fake News!")
    denun.julgar(j1, 'O denunciado é obrigado a pagar uma multa ao denunciante!')
    print(denun)
