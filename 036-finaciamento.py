c = float(input('Informe o valor da casa a ser financiada: R$'))
s = float(input('Informe o seu salário: R$'))
a = int(input('Informe a quantidade de anos pagando as parcelas: '))
sn = s * 0.30
m = a * 12
v = sn * m
w = c / m
if v >= c:
    print('Seu financiamento foi aprovado, as parcelas serão de R${:.2f}'.format(w))
else:
    print('Negado apenas.')
