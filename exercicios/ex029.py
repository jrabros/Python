v = int(input('Qual é a velocidade do carro? '))
multa = (v - 80) * 7

if v > 80:
    print('Você ultrapassou a velocidade e está {}km/h acima do permitido foi multado por R${}'.format(v-80, multa))
else:
    print('Tudo ok')