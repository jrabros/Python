palavras = (
    'Menu',
    'Garçom',
    'Chefe',
    'Reserva',
    'Sobremesa',
    'Talher',
    'Taça',
    'Bebida',
    'Acompanhamento',
    'Conta',
    'Prato',
    'Apetite',
)
for palavra in palavras:
    print()
    print(f'Na palavra {palavra.upper()} temos ', end=' ')
    for letra in palavra:
        if letra in "AEIOUaeiou":
            print(letra.lower(), end=' ')