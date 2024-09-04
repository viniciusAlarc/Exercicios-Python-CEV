'''
Crie um programa que leia vários números no teclado. No final da execução, mostre a média entre todos os valores e qual foi
o maior e o menor valores lidos. O programa deveperguntar ao usuário se ele que ou não continuar a digitar valores.
'''
cont = 0
soma = 0
maior = 0
menor = 0

print('Esse programa calcula a média de uma série de números e informa o maior e o menor.')
while True:
    num = float(input('Numero: '))
    if num == 0:
        break
    soma = soma + num
    if menor == 0:
        menor = num
    if maior == 0:
        maior = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    cont += 1

print('Media: {:.2f}'.format(soma / cont), end='')
print('''
Maior: {}
Menor: {}
'''.format(maior, menor))
