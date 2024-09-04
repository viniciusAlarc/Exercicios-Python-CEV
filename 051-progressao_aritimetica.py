termoX = int(input('Informe quantos termos você quer que a PA possua: '))
print('=' * 26)
print('   {} TERMOS DE UMA PA'.format(termoX))
print('=' * 26)
inicio = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
formula = inicio + (termoX-1) * razao
for i in range(inicio, formula+1, razao):
    print(i, end=' --> ')
print('CABO.')

