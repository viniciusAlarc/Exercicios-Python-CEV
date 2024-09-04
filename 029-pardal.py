v = int(input('Informe a velocidade em que o carro estava quando passou pelo pardal em km/h: '))
if v > 1000:
    print('Maluco passou de jato, mas enfim, sua multa é de R${}'.format((v - 80) * 7))
else:
    if v < 0:
        print('Ué, tava andando de ré? kk')
    else:
        if v > 80:
            print('Você ultrapassou o limite de 80km/h, sua multa é de R$7 por km ultrapassado, ou seja, R${}'.format((v - 80) * 7))
        else:
            if v <= 80:
                print('Tudo certo, o limite de velocidade da via é de 80km/h e seu carro passou a {}km/h, portanto, sem multa.'.format(v))
