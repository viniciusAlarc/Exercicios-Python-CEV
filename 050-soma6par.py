print('Esse programa lê 6 números e soma apenas os nýmeros que forem par dentre eles.')
for c in range(0, 6):
    n = int(input('Digite um número: '))
    ty = n % 2
    tr = c % 2
    if ty and tr == 0:
        s = n+c
print('O resultado da soma foi de {}'.format(s))
