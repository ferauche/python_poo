from frota import *
def operar_carro(carro : Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

    print('Infos atuais do carro')
    print(carro)

if __name__ == "__main__":
    print('Cadastre o primeiro carro')
    nm_modelo1 = input('Digite o modelo: ')
    nm_marca1 = input('Digite a marca: ')
    nm_cor1 = input('Digite a cor: ')
    nm_litros1 = float(input('Tamanho do tanque: '))
    nm_cm1= float(input('Consumo do tanque: '))

    carro1 = Carro(nm_modelo1, nm_marca1, nm_cor1, 0, False, nm_litros1, nm_cm1)

    print('Cadastre um segundo carro')
    nm_modelo2 = input('Digite o modelo: ')
    nm_marca2 = input('Digite a marca: ')
    nm_cor2 = input('Digite a cor: ')
    nm_litros2 = float(input('Tamanho do tanque: '))
    nm_cm2 = float(input('Consumo do tanque: '))

    carro2 = Carro(nm_modelo2, nm_marca2, nm_cor2, 0, False, nm_litros2, nm_cm2)

    '''
    Controlando dois carro até atingir 600 Km
    '''
    while carro1.get_odometro() < 600 and carro2.get_odometro() < 600 and (carro1.get_tanque() > 0 or carro2.get_tanque()> 0):
        try:
            print('Escolha um carro:')
            print(f'Carro 1: {nm_modelo1} {nm_cor1}')
            print(f'Carro 2: {nm_modelo2} {nm_cor2}')
            op = 0
            while op not in (1, 2):
                op = int(input("Digite as opcoes[1 ou 2]: "))
            if op == 1:
                operar_carro(carro1)
            else:
                operar_carro(carro2)
        except Exception as e:
            print("Erro!")
            print(e)

    print(carro1)
    print(carro2)
    if carro1.get_odometro() > carro2.get_odometro():
        print(f'{nm_modelo1} {nm_cor1} chegou primeiro que o {nm_modelo2} {nm_cor2}')
    elif carro1.get_odometro() == carro2.get_odometro():
        print(f'{nm_modelo1} {nm_cor1} chegou ao mesmo tempo {nm_modelo2} {nm_cor2}')
    else:
        print(f'{nm_modelo2} {nm_cor2} chegou primeiro que o {nm_modelo1} {nm_cor1}')
