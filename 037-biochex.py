n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
1 - Converter para BINÁRIO
2 - Converter para OCTAL
3 - COnverter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} em binário é {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('{} em octal é {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('{} em hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Escolha entre uma das opções disponíveis.')
