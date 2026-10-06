def metade(n, format=False):
    metade = n / 2
    return metade if format is False else moeda(metade)


def dobro(n, format=False):
    dobro = n * 2
    return dobro if format is False else moeda(dobro)


def aumentar(n, q, format=False):
    soma = n * (q / 100) + n
    return soma if format is False else moeda(soma)


def reduzir(n, q, format=False):
    resul = n - (n * (q / 100))
    return resul if format is False else moeda(resul)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preço = 0 , aumento = 0, desconto = 0):
    import moeda
    print('''
--------------------------
    RESUMO DO VALOR
--------------------------
    ''')
    print(f'Preço analisado: {moeda.moeda(preço):>19}')
    print(f'Dobro do preço: {moeda.dobro(preço, True):>20}')
    print(f'{aumento}% de aumento: {moeda.aumentar(preço, aumento, True):>20}')
    print(f'{desconto}% de redução: {moeda.reduzir(preço, desconto, True):>20}')
