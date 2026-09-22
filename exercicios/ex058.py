import random
acertou = False
n2 = random.randint(0,10)
palpites = 1
while not acertou:
    n1 = int(input('Tente adivinhar o número entre 0 e 10: '))
    if n1 == n2:
        print('Parabéns, você acertou. -- {} --'.format(n2))
        print('E foram {} tentativas'.format(palpites))        
        acertou = True
    else:
        print('Errou, tente novamente')
        palpites += 1
