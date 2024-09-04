import time
# gracejo
print('\033[1;36m-*-'*9)
print('   CALACULADORA FATORIAL')
print('-*-'*9, '\033[m')
time.sleep(0.3)
print('.', end='')
time.sleep(0.3)
print('.', end='')
time.sleep(0.3)
print('.')
time.sleep(0.3)

# fatorial = x * (x - 1) ate que x seja multiplicado por 1
print('Bem vindo(a)!')
n = int(input('Dígite o número para acharmos o fatorial dele: '))
n_fixo = n
n_decrescente = n
print(n_fixo, end='')
if n == 1:
    print('! = 1')
elif n == 0:
    print('! = 1')
    print('SIM 0 fatorial é 1')
    print('yooooo')
else:
    for i in range(n-1):
        n_decrescente -= 1
        n = n * (n_decrescente)
        print(' (X {}) = {}'.format(n_decrescente, n), end='')
print('\nFatorial: {}'.format(n))
