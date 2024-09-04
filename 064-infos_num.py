''''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vau parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
'''
print('Nesse programa, você digita números infinitamente e no final ele mostra a soma e o número de termos... (Mas infinitamente não tem final, então o final é digitar 999)\n')
cont_vezes = 0
soma_numeros = 0
while True:
    num = int(input('Informe um número: '))
    if num == 999:
        break
    cont_vezes += 1
    soma_numeros += num
print('Qunatos números foram digitados: {}'.format(cont_vezes))
print('Soma dos números: {}'.format(soma_numeros))
