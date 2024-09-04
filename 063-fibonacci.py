# Sequência de Fbonacci: a soma dos dois últimos termos forma o próximo termo: 1 1 2 3 5 8 13 21 34 55 87 144
#F1 = 1, F2 = 1
#Fn = F(n-1) + F(n-2)
quantidade = int(input('Quantos termos da seqência de Fibonacci você deseja ver? '))
n1 = 0
n2 = 1
contagem = 0
if quantidade >= 0:
    while True:
        print(n1)
        contagem += 1
        soma = n1 + n2
        n2 = n1
        n1 = soma
        if contagem > quantidade-1:
            break
