d = int(input('Informe a distância da viagem em km: '))

if d > 200:
    print('Para viagens a cima de 200km de distâcia, o valor é de R$0.45/km, você terá que pagar R${}'.format(d * 0.45))
else:
    if d < 0:
        print('Como assim?')
    else:
        if d <= 200:
            print('O valor a se pagar para viagens de menos de 200km é de R$0.50/km, você terá que pagar R${}'.format(d * 0.50))
