from datetime import date
ano_atual = date.today().year
qnt_pessoas = int(input('Quantas pessoas terão suas idades analisadas? '))
maioridade = 0
menoridade = 0
for i in range (1, qnt_pessoas+1):
    ano_nasc = int(input('Informe o ano que a {}ª pessoa nasceu: '.format(i)))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        maioridade += 1
    else:
        menoridade +=1
if maioridade > 1 or maioridade == 0:
    print('Temos um total de {} pessoas na maioridade e {} fora dela'.format(maioridade, menoridade))
if maioridade == 1:
    print('Temos um total de {} pessoa na maioridade e {} fora dela'.format(maioridade, menoridade))
