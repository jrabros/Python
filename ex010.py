carteira = float(input('Quanto dinheiro você tem na carteira? '))
# Considerando dolar à R$5,15
res = carteira / 5.15
print('Você pode comprar {:.2f} em dolar'.format(res))