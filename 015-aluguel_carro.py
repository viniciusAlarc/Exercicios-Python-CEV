print('A quantia a se pagar pelo carro alugado se dá pelos \033[4mdias\033[m em que o carro foi usado e pela quantidade de \033[4mquilômetros\033[m que este percorreu')
print('A relação é a seguinte: \033[7;30mR$60 por dia\033[m e \033[7;30mR$0.15 por km\033[m')
d = int(input('O carro foi usado por quantos dias? '))
km = float(input('O carro percorreu quantos km? '))
p1 = d * 60
p2 = km * 0.15
a = p1 + p2
print('O preço a ser pago pelo aluguel do carro é de \033[1;30mR${:.2f}\033[m'.format(a))
