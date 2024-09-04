from datetime import date
a = date.today().year
n = int(input('Informe o ano de nascimento do atleta: '))
i = a - n
print('O atleta tem {} anos.'.format(i))
if i < 0:
    print('Impossível.')
elif i <= 9:
    print('Categoria: MIRIM')
elif i <= 14:
    print('Categoria: INFANTIL')
elif i <= 19:
    print('Categoria: JUNIOR')
elif i <= 20:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
