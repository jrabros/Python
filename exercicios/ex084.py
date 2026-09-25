pessoas = list()
dados = list()
lista_pesados = list()
lista_leves = list()
maior = menor = 0
while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
         menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
            break

for c in pessoas:
    if c[1] < menor:
         menor = c[1]
    if c[1] > maior:
        maior = c[1]
    if c[1] >= 100:
        lista_pesados.append(c[0])
    elif c[1] <= 70:
        lista_leves.append(c[0])
print(f'''
Registrou {len(pessoas)} pessoas
O maior peso foi de {maior}. Peso de {lista_pesados}
O menor peso foi de {menor}. Peso de {lista_leves}
 ''')