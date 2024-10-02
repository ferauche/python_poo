class Carro:
    modelo : str
    marca : str
    cor : str
    __odometro = 0.0
    __motor_on = False

    def __init__(self, modelo : str, marca : str, cor : str,
                       odometro : float, motor : bool):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.__odometro = odometro
        self.__motor_on = motor

    def ligar(self):
        if not self.__motor_on:
            self.__motor_on = True
        else:
            raise Exception("Erro: Motor já ligado!")

    def acelerar(self, velocidade : float, tempo : float):
        if self.__motor_on:
            self.__odometro += velocidade * tempo
        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

    def desligar(self):
        if self.__motor_on:
            self.__motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def get_odometro(self):
        return self.__odometro

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.__odometro} Km, '
                f'motor {self.__motor_on}')
        return info





