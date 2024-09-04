'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs.: Considere que o caixa possui cédulas de R$100, R$50, R$20, R$10, R$5, R$2, R$1
'''
print('+'*30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('+'*30)
valor = int(input('De quanto precisa? R$'))
cedula = 100
totcedula = 0
while True:
    if valor >= cedula:
        valor-= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'Total de {totcedula} cédulas de R${cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totcedula = 0
        if valor == 0:
            break