import math

ca = float(input('Qual o valor da Cateto Adjacente: '))
co = float(input('Qual o valor da Cateto Oposto: '))

h = math.hypot(ca, co)

print('Hipotenusa é {:.2f}'.format(h))