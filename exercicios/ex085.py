numeros = list()
pares = list()
impares = list()
for c in range(1,8):
    n = int(input(f'Digite {c}º número: '))
    numeros.append(n)
for c in numeros:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
impares.sort()
pares.sort()
print(f'Os valores impares são: {impares}')
print(f'Os valores pares são: {pares}')