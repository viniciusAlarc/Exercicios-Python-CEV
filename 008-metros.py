m = int(input('Digite o comprimento em metros (m): '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
v = {'l': '\033[m', '4': '\033[4m'}
print('O valor em quilômetros (km) é {}{:.2f}{}'.format(v['4'], km, v['l']))
print('O valor em hectômetros (hm) é {}{:.2f}{}'.format(v['4'], hm, v['l']))
print('O valor em decâmetros (dam) é {}{:.2f}{}'.format(v['4'], dam, v['l']))
print('O valor em decímetros (dm) é {}{:.2f}{}'.format(v['4'], dm, v['l']))
print('O valor em centímetros(cm) é {}{:.2f}{}'.format(v['4'], cm, v['l']))
print('O valor em milímetros (mm) é {}{:.2f}{}'.format(v['4'], mm, v['l']))
