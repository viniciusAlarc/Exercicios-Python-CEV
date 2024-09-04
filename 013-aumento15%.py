x = float(input('Informe seu salário: R$'))
print('O salário após o aumento de \033[30m15%\033[m, seu salário será R$\033[32m{:.2f}\033[m'.format(x*1.15))
