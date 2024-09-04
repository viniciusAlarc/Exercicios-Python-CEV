'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário quer continuar.
No final mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato
'''
total = 0
maisdemil = 0
contador = 0
maisbarato = None
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: '))
    total += preço
    contador += 1

    if preço > 1000:
        maisdemil += 1
    if contador <= 1:
        maisbarato = preço
    if preço < maisbarato:
        maisbarato = preço
    if maisbarato == preço:
        nomemb = nome

    teste = str(input('Deseja continuar? [S/N] '))
    if teste == 'N' or teste == 'n':
        break

print(f'Total gasto {total}')
print(f'Produtos que custaram mais de R$ 1000: {maisdemil}')
print((f'Produto mais barato: {nomemb}'))
