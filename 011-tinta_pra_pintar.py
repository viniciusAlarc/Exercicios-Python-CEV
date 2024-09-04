b = float(input('Informe o comprimento da base da parede em metros: '))
h = float(input('Informe o comprimento da altura da parede em metros: '))
a = b * h
t = a / 2
print('Você precisará de \033[4m{}\033[m litros de tinta para pintar essa parde'.format(t))
