from random import choice
a = input('Informe o nome do primeiro aluno: ')
b = input('Informe o nome do segundo aluno: ')
c = input('Informe o nome do terceiro aluno: ')
d = input('Informe o nome do quarto aluno: ')
lista = [a, b, c, d]
esc = choice(lista)
print('O aluno sorteado para apagar o quadro foi {}.'.format(esc))
