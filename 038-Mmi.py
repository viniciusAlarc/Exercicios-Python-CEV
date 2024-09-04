n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('{} é menor que {}'.format(n1, n2))
else:
    print('Os números são iguais')
