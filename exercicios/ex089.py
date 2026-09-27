lista = []
dados = []
while True:
    dados.append(str(input('Qual o nome do aluno: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    média = (dados[1] + dados[2]) / 2
    dados.append(média)
    lista.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-' * 10)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, c in enumerate(lista):
    print(f'{i:<4}{c[0]:<10}{c[3]:>8.2f}')
while True:
    indice = int(input('Qual aluno gostaria de ver as notas? (999 encerra solicitações) '))
    if indice == 999:
        break
    if indice <= len(lista):
        print(f'As notas de {lista[indice][0]} são: {lista[indice][1]} e {lista[indice][2]}')

