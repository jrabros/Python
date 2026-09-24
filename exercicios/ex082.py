lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Nn':
        break
for p, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(lista)
print(par)
print(impar)
