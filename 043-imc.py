a = float(input('Informe a sua altura: '))
p = float(input('Informe o seu peso: '))
imc = p / (a**2)
if imc > 0:
    print('IMC: {:.2f}'.format(imc))
    if imc < 17:
        print('Status: Muito abaixo do peso')
    elif imc <= 18.49:
        print('Status: Abaixo do peso')
    elif imc <= 24.99:
        print('Status: Dentro do peso ideal')
    elif imc < 30:
        print('Status: Sobrepeso')
    elif imc < 35:
        print('Status: Obesidade')
    elif imc <= 40:
        print('Status: Obesidade severa')
    elif imc > 40:
        print('Status: Obesidade mórbida')
else:
    print('Como?')
