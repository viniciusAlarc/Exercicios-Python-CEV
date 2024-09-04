from random import randint
from time import sleep
print('-=-' * 15)
print('     Vou pensar em um número de 0 a 5...')
print('-=-' * 15)
n = int(input('Será que você advinha qual é? \nDeixe seu palpite: '))
print('_' * 44)
print('PROCESSANDO...')
sleep(2)
s = randint(0, 5)
if n == s:
    print('Parabéns, você acertou! O número em que pensei foi {} (maldito, me venceu)'.format(s))
else:
    print('Que pena, você errou... O número em que pensei foi {}, não {} (kkk ganhei).'.format(s, n))
