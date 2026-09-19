import random
n1 = random.randint(1,5)
n2 = int(input('Digite um número de 1 a 5: '))
if n1 == n2:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! O número correto era {}.'.format(n1))