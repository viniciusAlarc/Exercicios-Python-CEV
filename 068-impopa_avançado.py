'''
Faça um programa que jogue par ou ímpar com o computador, o jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que o jogador conquistou no final do jogo
'''
from random import randint
print('='*10)
print('IMPOPA')
print('='*10)
v = 0
while True:
    sorte = randint(1, 10)
    impopa = str(input('Você vai querer impa ou pa...? [I/P] '))
    impopa_format = impopa.lower()
    num = int(input('Escolha seu número: '))
    teste = (sorte + num) % 2
    print(f'Eu escolho {sorte}!')
    if teste == 0:
        if impopa_format == 'i':
            print(f'PERDEU, deu {sorte+num}')
            break
        elif impopa_format == 'p':
            print(f'Deu {sorte+num}... você venceu... vamo mais uma >:[')
            v += 1
        else:
            print('Calmai que alguma coisa deu errado...')
    elif teste == 1:
        if impopa_format == 'p':
            print(f'PERDEU, deu {sorte+num}')
            break
        elif impopa_format == 'i':
            print(f'Deu {sorte+num}... você venceu... vamo mais uma >:[')
            v += 1
        else:
            print('Calmai que alguma coisa deu errado...')
print(f'GAME OVER! \nNúmero de vitótias: {v}')
print('_'*30)
