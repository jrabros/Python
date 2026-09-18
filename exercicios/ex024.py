cidade = input('Digite nome da cidade: ')
cidade = cidade.capitalize().split()[0]
if ('Santo' in cidade) == True:
    print('começa com Santo')
else:
    print('A palavra Santo NÃO está no primeiro nome da cidade')