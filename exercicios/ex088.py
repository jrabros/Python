from random import randint
from time import sleep
lista = []
jogos = []
quant = int(input('Quantos jogos você quer fazer? '))
tot = 0
while quant > tot:
    count = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            count += 1
        if count > 5:
            break        
        lista.sort()

    jogos.append(lista[:])
    lista.clear()
    quant -= 1
for c in range(0, len(jogos)):
    print(f'Jogo {c+1}: {jogos[c]}')
    sleep(1)
