'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastradas, o programa deverá perguntar
se o usuário quer ou não continuar. No final mostre:
A) Quantas pessoas têm mais de 18 anos
B) Quantos homens foram cadastrados
C) Quantas mulheres têm menos de 20 anos
'''

print('Esse programa lê idade e sexo de múltiplo usuários e depois informa alguns dados sobre os usuários informados.')
letraA = 0
letraB = 0
letraC = 0
while True:
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        letraA += 1
    if sexo == 'M':
        letraB += 1
    if sexo == 'F' and idade < 20:
        letraC += 1
    confirm = input(str('Deseja continuar? [S/N] ')).strip().upper()[0]
    if confirm == 'N':
        break
print(f'''
- Pessoas com mais de 18 anos: {letraA}
- Homens cadastrados: {letraB}
- Mulheres com menos de 20 anos: {letraC}
''')

