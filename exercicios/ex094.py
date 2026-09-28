lista = list()
dados = dict()
média = totidade = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        else:
            print('ERRO! M ou F')
    dados['idade'] = int(input('Idade: '))
    totidade += dados['idade']
    lista.append(dados.copy())
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
média = totidade / len(lista)
print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'Média é {média}')
print(f'As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f"p['nome'] ", end='')
print()
print('A lista de pessoas acima da idade média: ', end='')
for p in lista:
    if p['idade'] > média:
        print(f"p['nome'] ", end='')
print()