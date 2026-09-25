dados = list()
dados.append('Pedro')
dados.append(25)
pessoas = list()
pessoas.append(dados[:])
dados[0] = 'João'
dados[1] = 15
pessoas.append(dados[:])
dados[0] = 'Andi'
dados[1] = 31
pessoas.append(dados[:])
print(pessoas)