from time import sleep
n = int(input('Quer saber a tabuada de qual número? '))
print('Está é a tabuada de {}'.format(n))
sleep(0.5)
for c in range(1, n+1):
    s = c * n
    print('{} x {} = {}'.format(n, c, s))
