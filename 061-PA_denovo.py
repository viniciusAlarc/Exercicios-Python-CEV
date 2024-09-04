inicio = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = inicio
contagem = 0
while contagem < 10:
    print(termo)
    termo+= razão
    contagem += 1
