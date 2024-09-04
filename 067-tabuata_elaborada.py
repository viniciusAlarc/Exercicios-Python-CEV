'''
Faça um programa que mostre a tabuata de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''
print('Esse prgrama informa a tabuada de qualquer número, para finalizar a execução, basta digitar um número negativo.')
while True:
    num = int(input('Informe um número: '))
    if num < 0:
        break
        print('erro')
    for c in range (1, 11):
        print(f'{num} x {c} = {num * c}')
