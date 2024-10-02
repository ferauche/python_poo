from Interface_Eleicao import *
from typing import List
from common import *
import csv

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

    def get_denunciante(self):
        return self.__denunciante

    def get_denunciado(self):
        return self.__denunciado

    def get_juiz(self):
        return self.__juiz

    def get_txt_sentenca(self):
        return self.__txt_sentenca

    def get_txt_denuncia(self):
        return self.__txt_denuncia

class Jurisprudencia(Transparencia):
    ano : int
    denuncias : List[Denuncia]

    def __init__(self, a:int):
        self.ano = a
        self.denuncias = []

    def add_denuncia(self, d: Denuncia):
        self.denuncias.append(d)

    def to_csv(self):
        with open(f'juris_{self.ano}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Denunciante', 'Denunciado', 'Denuncia', 'Sentença', 'Juiz'])

            for denuncia in self.denuncias:
                writer.writerow([denuncia.get_denunciante().get_nome(), denuncia.get_denunciado().get_nome(),
                                 denuncia.get_txt_denuncia(), denuncia.get_txt_sentenca(),
                                 denuncia.get_juiz().get_nome()])

    def to_txt(self):
        with open(f'juris_{self.ano}.txt', mode='w') as file:
            for denuncia in self.denuncias:
                file.write(denuncia.__str__())


if __name__ == "__main__":
    j1 = Juiz("Alex Morales", "12312", 123123, 4456)
    #p1 = Pessoa("Jose", 123123, 123123)
    c1 = Candidato("ADADADA", "223", "23123", 1)
    c2 = Candidato("xxxxxxx", "333", "444", 2)
    denun = Denuncia(1, c1, c2, "Fake News!")
    denun.julgar(j1, 'O denunciado é obrigado a pagar uma multa ao denunciante!')
    juris1 = Jurisprudencia(2024)
    juris1.add_denuncia(denun)
    juris1.to_csv()
    juris1.to_txt()
    print(denun)
