print('\033[7m{:=^40}'.format(' VAINUS ENTERPRISESES '))
v = float(input('\033[mQual é o preço das compras?: R$'))
print('1- Pagando no dinheiro ou cheque, \033[32mo ptoduto terá 10% de desconto\033[m.')
print('2- Pagando no cartão á vista, \033[33mo produto terá 5% de desconto\033[m.')
print('3- Pagando no cartão em até 2x, \033[30mo produto terá seu preço normal (sem descontos ou juros)\033[m.')
print('4- Pagando no cartão em 3x ou mais, \033[31mserá cobrado um juros de 20% em cima do valor original\033[m.')
p = input('Escolha uma forma de pagamento entre \033[32m{}\033[m, \033[33m{}\033[m, \033[30m{}\033[m ou \033[31m{}\033[m: '.format('1', '2', '3', '4'))
print('')
print('\033[7m-=-\033[m'*35)
if p == '1':
    print('\nPagando no dinheiro ou cheque, o preço será R${:.2f}'.format(v*0.90))
elif p == '2':
    print('\nPagando no cartão em 1x, o preço será R${:.2f}'.format(v*0.95))
elif p == '3':
    print('\nPagando no cartão em até 2x, o preço será o mesmo que o original, portanto, duas parcelas R${:.2f}'.format(v/2))
elif p == '4':
    print('\nPagando no cartão em 3x ou mais, o preço terá 20% de juros, portanto será de R${:.2f} no total'.format(v*1.20))
    par = int(input('Será dividido em quantas vezes? '))
    if par < 3:
        print('Uai')
    else:
        print('Cada parcela será de R${:.2f}'.format((v*1.20)/par))
else:
    print('\nOpção inválida, escolha entre uma das quatro possíveis (1, 2, 3, 4)')
