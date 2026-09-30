def area(largura, comprimento):
    area = l * c
    print(f'A área do terreno {l}x{c} é de {area:.2f}m²')


print('Controle de Terrenos')
print('-' * 25)
l = float(input('Qual é a largura do terreno (m): '))
c = float(input('Qual é o comprimento do terreno (m): '))
area(l,c)