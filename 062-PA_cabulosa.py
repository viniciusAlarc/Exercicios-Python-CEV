termoX = int(input('Informe quantos termos você quer que a PA possua: '))
inicio = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
contagem = 0
while True:
    contagem += 1
    formula = inicio + (contagem - 1) * razão
    print(formula)
    if contagem > termoX-1:
        confirmação = int(input('Deseja que sejam exibidos mais quantos termos? '))
        if confirmação == 0:
            break
        termoX += confirmação
print('CABOSSE')
print('Número de termos: {}'.format(contagem))
