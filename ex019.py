import random
nomes = ['João', 'Bruno', 'Andi', 'Anne']
print('{}'.format(nomes))
print('O escolhido foi {}'.format(random.choice(nomes)))

#ex20
random.shuffle(nomes)
print('A ordem é {}'.format(nomes))