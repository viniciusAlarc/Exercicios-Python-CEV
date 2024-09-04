print('Esse programa caucula o aumento no seu salário, sendo 15% de aumento para menos de R$1250 e 10% para mais>')
s = float(input('Informe seu salário em R$: '))
if s > 1250:
    print('Seu salário com o aumento é de {}'.format(s + (s*0.10)))
else:
    print('Seu salário com o aumento é de {}'.format(s + (s*0.15)))
