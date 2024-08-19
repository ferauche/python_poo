class Carro:
    modelo : str
    marca : str
    cor : str
    odometro : 0.0
    motor_on : False
    tanque: float
    consumo_medio: float

    def __init__(self, modelo : str, marca : str, cor : str,
        odometro : float, motor : bool, tanque : float, cpnsumo_medio : float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.odometro = odometro
        self.motor_on = motor
        self.tanque = tanque
        self.consumo_medio = cpnsumo_medio

    def ligar(self):
        if not self.motor_on and self.tanque>0:
            self.motor_on = True
        else:
            raise Exception("Erro: Motor já ligado! ou Sem Combstível")

    def acelerar(self, velocidade : float, tempo : float):
        if self.motor_on:
            km = velocidade*tempo
            litros=km/self.consumo_medio
            if self.tanque>litros:
                self.tanque-=litros
                self.odometro+=km
            else:
                self.odometro+=self.tanque*self.consumo_medio
                self.tanque=0
                self.motor_on = False
        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

    def desligar(self):
        if self.motor_on:
            self.motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.odometro} Km, '
                f'motor {self.motor_on}\n'
                f'consumo {self.consumo_medio} Km/L'
                f'nivel do tanque {self.tanque} L')
        return info





