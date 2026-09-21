n1 = int(input('Qual o primeiro termo: '))
n2 = int(input('Qual a razão? '))
decimo = n1 + (10 - 1) * n2
for c in range (n1, decimo + n2 ,n2):
    print('{}'.format(c))