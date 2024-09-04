while True:
    n1 = float(input('Informe o primeiro número: '))
    n2 = float(input('Informe o segundo número: '))

    print('''
    Digite um dos números abaixo para realizar o comando
    
    [1] Somar 
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    resposta = input('Opção: ')
    if resposta == '1':
        print('A soma é {}'.format(n1+n2))
    elif resposta == '2':
        print('A Múltiplicação é {}'.format(n1*n2))
    elif resposta == '3':
        if n1 > n2:
            print('O maior dentre eles é {}'.format(n1))
        elif n1 < n2:
            print('O maior dentre eles é {}'.format(n2))
        elif n1 == n2:
            print('Ambos são iguais... Não tem maior.')
    elif resposta == '4':
        print('Voltando...')
    elif resposta == '5':
        print('Adeus.')
        break