from random import randint
print('-=-' * 15)
print('    Vou pensar em um número de 0 a 1000')
print('-=-' * 15)
palpite = int(input('Vamos ver em quanto tempo você acerta... \nDeixe seu palpite: '))
resposta = randint(0, 1000)
cont = 0
while palpite != resposta:
    cont += 1
    if palpite > resposta:
        print('Menos...')
    elif palpite < resposta:
        print('Mais...')
    palpite = int(input('Deixe seu palpite: '))
if cont < 2:
    print('TAPORAAAAAAA\n DE PRIMEIRAAAAAAAAA\n Uma chance de 0 em 1000.... Como se sente?')
else:
    print('ACERTOU....')
    print('E só precisou de {} tentativas.'.format(cont+1))
