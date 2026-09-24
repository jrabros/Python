# MODELOS PARA RETIRAR UM ITEM DA LISTA
# del.lanche[x]
# .pop(x)
# .remove('')
# .pop() -> vai remover o ultimo item


#ACRESCENTAR 
# .append(x)

# CRIAR LISTA À PARTIR DO RANGE -> valores = list(range(4,11)) -> valor de 4 à 10

# para valores.sort() -> organiza em ordem
# valores.sort(reverse=True) -> organiza ordem decrescente
valores = []
for count in range(0,5):
    valores.append(int(input('Digite o valor: ')))
for c, v in enumerate(valores):
    print(f'Encontrei o valor {v} na posição {c}')

# AS LISTAS TEM LIGAÇÃO
# COPIA B = A[:]