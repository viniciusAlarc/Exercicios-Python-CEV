numero = int(input('Digite um número para descobrir se é um número primo: '))
total = 0
for c in range(1, numero +1):
    if numero % c == 0:
        print('\033[32m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(numero, total))
if total == 2:
    print('É PRIMO')
else:
    print('NÃO É PRIMO')
