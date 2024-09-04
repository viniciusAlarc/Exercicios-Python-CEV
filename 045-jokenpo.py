from random import randint
from time import sleep
print('—'*10)
print('    JOKENPO')
print('—'*10)
print('Escolha entre pedra, papel ou tesoura.')
e = str(input('O que vai ser? '))
s = randint(0, 2)
em = e.lower()
print('Eu jogo', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)
if s == 0:
    print('Pedra')
elif s == 1:
    print('Papel')
elif s == 2:
    print('Tesoura')
if (em == 'pedra' and s == 0) or (em == 'papel' and s == 1) or (em == 'tesoura' and s == 2):
    print('Ah, empatou.')
elif (em == 'pedra' and s == 1) or (em == 'papel' and s == 2) or (em == 'tesoura' and s == 0):
    print('HA! Ganhei, fraco.')
elif (em == 'pedra' and s == 2) or (em == 'papel' and s == 0) or (em == 'tesoura' and s == 1):
    print('Oh shit. Ganhou, parabéns aí (irônia).')
else:
    print('Escolha entre uma das opções aí.')
