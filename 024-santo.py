c = str(input('Digite o nome da sua cidade: ')).strip()
print('Sua cidade começa com "Santo"?')
print('santo' in c.lower()[:5])
