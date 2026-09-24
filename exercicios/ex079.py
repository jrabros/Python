valores = []
while True:
    n = (int(input('Digite um valor: ')))
    if n in valores:
        print('Valor já existe, não vou adicionar')
    else:
        valores.append(n)
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'nN':
        break
valores.sort()
print(f'{valores}')