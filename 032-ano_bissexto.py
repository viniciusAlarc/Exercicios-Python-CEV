from datetime import date
ano = int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual. '))
a = ano % 400
b = ano % 100
c = ano % 4
if ano == 0:
    ano = date.today().year
if a == 0:
    print('{} é um ano bissexto.'.format(ano))
else:
    if b == 0:
        print('{} não é um ano bissexto.'.format(ano))
    else:
        if c == 0:
            print('{} é um ano bissexto.'.format(ano))
        else:
            print('{} não é um ano bissexto'.format(ano))
