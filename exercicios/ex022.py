nome = str(input('Qual o seu nome completo? '))
print('{}'.format(nome.upper()))
print('{}'.format(nome.lower()))
total = len(nome.replace(' ', ''))
print(total)
primeiro = nome.split()[0]
print('{}'.format(len(primeiro)))