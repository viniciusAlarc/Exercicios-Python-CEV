print('\033[7;30m-'*30)
print('  ANALISADOR DE TRÂNGULOS')
print('-'*30)
r1 = float(input('\033[mInforme o valor da reta 1: '))
r2 = float(input('Informe o valor da reta 2: '))
r3 = float(input('Informe o valor da reta 3: '))
v1 = r1 + r2
v2 = r2 + r3
v3 = r3 + r1
if v1 > r3:
    if v2 > r1:
        if v3 > r2:
            print('Com as 3 retas, \033[32mé possível\033[m formar um triângulo.')
        else:
            print('Com as 3 retas, \033[31mnão é possível\033[m formar um triângulo.')
    else:
        print('Com as 3 retas, \033[31mnão é possível\033[m formar um triângulo.')
else:
    print('Com as 3 retas, \033[31mnão é possível\033[m formar um triângulo.')
