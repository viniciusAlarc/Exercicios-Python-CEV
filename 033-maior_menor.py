n1 = int(input('Infome o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
if n1 > n2 and n1 > n3:
    print('{} é o maior número.'.format(n1))
else:
    if n2 > n1 and n2 > n3:
        print('{} é o maior número.'.format(n2))
    else:
        if n3 > n1 and n3 > n2:
            print('{} é o maior número.'.format(n3))
if n1 < n2 and n1 < n3:
    print('{} é o menor número.'.format(n1))
else:
    if n2 < n1 and n2 < n3:
        print('{} é o menor número.'.format(n2))
    else:
        if n3 < n1 and n3 < n2:
            print('{} é o menor número.'.format(n3))
