n = str(input('Informe seu nome completo: ')).strip()
k = n.split()
print('Primeiro nome: {}'.format(k[0]))
print('Último nome: {}'.format(k[len(k)-1]))
