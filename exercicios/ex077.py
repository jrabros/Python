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
    print(f'\nNa palavra {palavra.upper()} temos ', end=' ')
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra.lower(), end=' ')