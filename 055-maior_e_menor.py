quantidade = int(input('Quantos dados serão analisados? '))
menor = float(0)
maior = float(0)
for i in range (1, quantidade+1):
    dados = float(input('Informe o {}º valor: '.format(i)))
    if maior == 0:
        maior = dados
    if menor == 0:
        menor = dados
    else:
        if dados > maior:
            maior = dados
        elif dados < menor:
            menor = dados
print('Maior: ', maior)
print('Menor: ', menor)
