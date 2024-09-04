print('Essa é a soma dos números ímpar múltiplos de 3 no intervalo de 1 a 500')
for c in range(0, 501, 3):
    s = c // 2
    if s != 0:
        print(s)
