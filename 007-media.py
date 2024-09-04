n1 = float(input('Digite a nota 1: '))
if n1 > 10:
    print('Não dá pra tirar mais que 10, vem com essa não.')
else:
    if n1 < 0:
        print('Cacetada, como você tirou uma nota negativa?')
    else:
        n2 = float(input('Digite a nota 2: '))
        if n2 > 10:
            print('Não dá pra tirar mais que 10, vem com essa não.')
        else:
            if n2 < 0:
                print('Cacetada, como você tirou uma nota negativa?')
            else:
                print('A média é \033[7;30m{:.2f}\033[m'.format((n1+n2) / 2))
