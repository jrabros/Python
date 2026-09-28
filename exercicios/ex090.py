dicionario = dict()
dicionario['nome'] = str(input('Nome: '))
dicionario['media'] = float(input(f'Média de {dicionario["nome"]}: '))
if dicionario['media'] >= 7:
    dicionario['situacao'] = 'Aprovado'
else:
    dicionario['situacao'] = 'Reprovado'
for k, v in dicionario.items():
    print(f'{k} é igual {v}')