x = float(input('Informe o preço original do produto: R$'))
print('Esse produto com \033[30m5%\033[m de desconto custa R$\033[32m{:.2f}\033[m'.format(x*0.95))
