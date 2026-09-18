preco = float(input('Qual o preço do produto? '))
novo_preco = preco - (preco * 0.05)
print('O valor com 5% de desconto é R${:.2f}'.format(novo_preco))