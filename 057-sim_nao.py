print('''
SIM = S
NÃO = N
''')
reposta = str(input('S ou N? ')).upper().strip()
while reposta not in 'SN':
    reposta = str(input('S ou N? ')).upper().strip()

if reposta == 'S':
    print('SIM')
elif reposta == 'N':
     print('NÃO')
