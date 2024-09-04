a = str(input('Escreva uma frase qualquer: ')).lower().strip()
print('A letra "a" aparece {} vezes no seu texto.'.format(a.count('a')))
print('O primeiro "a" está na posição {}'.format(a.find('a')+1))
print('O último "a" está na posição {}'.format(a.rfind('a')+1))
