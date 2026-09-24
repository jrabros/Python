valores = []
for count in range(0,5):
    valores.append(int(input(f'Digite {count+1}º o valor: ')))
maior = max(valores)
menor = min(valores)
print(maior)
print(menor)