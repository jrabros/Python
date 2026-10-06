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