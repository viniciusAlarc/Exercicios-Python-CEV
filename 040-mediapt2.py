n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if (n1 < 0 or n1 > 10) or (n2 < 0 or n2 > 10):
    print('Como?')
elif m < 5:
    print('\033[0;31mReprovado\033[m ({:.2f})'.format(m))
elif m >= 7:
    print('\033[0;32mAprovado\033[m ({:.2f})'.format(m))
else:
    print('\033[0;33mRecuperação\033[m ({:.2f})'.format(m))
