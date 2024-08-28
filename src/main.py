from frota import *
def controlar_carro(carro: Carro ):
    print('1 -LIgar motor')
    print('2 - Desligar motor')
    print('3 - Acelerar')

    op = 0
    while op not in (1, 2 , 3):
        op = int(input("Digite as opcoes[1-3]: "))
    if op == 1:
        carro.ligar ()
    elif op == 2:
        carro.desligar ()
    elif op == 3:
        v = float(input("Informe a velocidade :"))
        t = float(input("Informe o tempo :"))
        carro.acelerar (v,t)

    print("Infos carro atual")
    print(carro)

if __name__ == "__main__":
    print('Cadastre o primeiro carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input('Litros do tanque: '))
    consu = float(input('Consumo medio: '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0 ,False, litros, consu)

    print('Cadastre o segundo carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input('Litros do tanque: '))
    consu = float(input('Consumo medio: '))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0 ,False, litros, consu)
    '''
    Controlando o carro até ele atingir 10000 Km
    '''
    while carro1.get_odometro() < 600 and carro2.get_odometro() < 600 and (carro1.get_tanque() > 0) or (carro2.get_tanque() > 0):
        try:
            op_carro = 0
            while op_carro not in [1, 2]:
                op_carro = int(input("Qual carro deseja controlar ? [1,2]:"))
            if op_carro == 1:
                controlar_carro(carro1)
            elif op_carro == 2:
                controlar_carro(carro2)

        except Exception as e:
            print("Erro")
            print(e)