from datetime import date
aa = date.today().year
s = str(input('Você é do sexo masculino ou feminino? '))
sm = s.lower()
if s == 'feminino':
    print('Por ser uma mulher, você não é legalmente obrigada a se alistar.')
elif s == 'masculino':
    an = int(input('Informe o ano em que você nasceu: '))
    i = aa - an
    if i < 0:
        print('Impossível...')
    else:
        if i == 18:
            print('Tá na hora de se alistar!')
        elif i < 18:
            tf = 18 - i
            al = tf + aa
            if tf > 1:
                print('Ainda não está na hora de se alistar, faltam {} anos.\nOu seja, você terá que se alistar em {}.'.format(tf, al))
            else:
                print('Ainda não está na hora de se alistar, falta {} ano.\nOu seja, você terá que se alistar em {}.'.format(tf, al))
        elif i > 18:
            tp = i - 18
            al = tp - aa
            if tp > 1:
                print('Seu tempo de se alistar já passou, foi há {} anos.\nOu seja, você deveria se alistar ou se alistou em {}.'.format(tp, al*-1))
            else:
                print('Seu tempo de se alistar já passou, foi há {} ano.\nOu seja, você deveria se alistar ou se alistou em {}.'.format(tp, al * -1))
else:
    print('Biologicamente falando, pode pôr...')
