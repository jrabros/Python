d = float(input('Qual a distancia da viagem? (KM)'))
if d <= 200:
    p = 0.50 * d
    print('O valor desta viagem será de R${}'.format(p))
else:
    p = 0.45 * d
    print('O valor desta viagem será de R${}'.format(p))