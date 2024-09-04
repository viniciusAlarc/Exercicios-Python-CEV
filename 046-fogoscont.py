from time import sleep
print('Os fogos de artifício serão lançados em...')
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[31mBOOOM!\033[m')
