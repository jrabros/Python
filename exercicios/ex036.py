casa = float(input('Qual o valor da casa? '))
salario = float(input('Quanto é seu salário? '))
tempo = float(input('Em quanto anos você vai pagar? '))

meses = tempo * 12
prestacao = casa / meses
limite = salario * (30/100)

if limite > prestacao:
    print('O valor da prestação é de R${:.2f}'.format(prestacao))
else:
    print('O valor da prestação é R${:.2f} e é maior do que 30% do seu salário que fica no valor de R${:.2f}. financiamento REPROVADO'.format(prestacao, limite))