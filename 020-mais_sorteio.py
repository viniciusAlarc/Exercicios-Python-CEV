from random import shuffle
a1 = input('Informe o nome do primeiro aluno: ')
a2 = input('Infore o nome do segundo aluno: ')
a3 = input('Informe o nome do terceiro aluno: ')
a4 = input('Informe o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))
