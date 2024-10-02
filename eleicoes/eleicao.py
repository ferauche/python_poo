import pickle
from typing import List
from common import *
from Interface_Eleicao import Transparencia
import csv

class Urna(Transparencia):
    mesario : Pessoa
    __secao : int
    __zona : int
    __eleitores_presentes : List[Eleitor] = []
    __votos = {} #dicionario chave = numero do candidato, valor é a quantidade de votos

    def __init__(self, mesario : Pessoa, secao : int, zona : int,
                 candidatos : List[Candidato], eleitores : List[Eleitor]):
        self.mesario = mesario
        self.__secao = secao
        self.__zona = zona
        self.__nome_arquivo = f'{self.__zona}_{self.__secao}'
        self.__candidatos = candidatos
        self.__eleitores = []
        for eleitor in eleitores:
            if eleitor.zona == zona and eleitor.secao == secao:
                self.__eleitores.append(eleitor)

        for candidato in self.__candidatos:
            self.__votos[candidato.get_numero()] = 0
        self.__votos['BRANCO'] = 0
        self.__votos['NULO'] = 0

        with open(self.__nome_arquivo+'.pkl', 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def get_eleitor(self, titulo : int):
        for eleitor in self.__eleitores:
            if eleitor.get_titulo() == titulo:
                return eleitor
        return False

    def get_zona(self):
        return self.__zona

    def get_secao(self):
        return self.__secao

    def registrar_voto(self, eleitor : Eleitor, n_cand : int):
        self.__eleitores_presentes.append(eleitor)
        if n_cand in self.__votos:
            self.__votos[n_cand] += 1
        else:
            self.__votos['NULO'] += 1

        with open(self.__nome_arquivo+'.pkl', 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def __str__(self):
        info =  f'Urna da seção {self.__secao}, zona {self.__zona}\n'
        info += f'Mesario {self.mesario}\n'
        return info

    def to_csv(self):
        with open(self.__nome_arquivo+'.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Seção', 'Zona', 'Eleitores Presentes'])
            for eleitor in self.__eleitores:
                writer.writerow([self.get_secao(), self.get_zona(), eleitor.get_titulo()])

    def to_txt(self):
        with open(self.__nome_arquivo+'.txt', mode='w') as file:
            file.write(f'{self.__str__()}\n')
            for eleitor in self.__eleitores:
                file.write(f'{eleitor.get_titulo()}\n')

if __name__ == "__main__":
    c1 = Candidato("ADADADA", "223", "23123", 1)
    c2 = Candidato("xxxxxxx", "333", "444", 2)
    e1 = Eleitor("Jorge Pascal", "12389172389", "129837", 123123, 23, 4)
    e2 = Eleitor("Olavo de Caralho", "9182738", "02984719", 343434, 23, 4)
    mesario = Eleitor("Orasmo Reis", "10298730987123", "1928469", 9889889, 23, 4)
    urna = Urna(mesario,23, 4, [c1, c2], [e1, e2])
    urna.to_txt()
    urna.to_csv()
