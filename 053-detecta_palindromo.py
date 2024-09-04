frase= str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('É um palíndromo!')
else:
    print('Não é um palindromo...')

