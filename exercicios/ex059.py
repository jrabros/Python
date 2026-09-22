t = 0
while t == 0:
    n1 = int(input('Qual o primeiro valor? '))
    n2 = int(input('Qual o segundo valor? '))
    print('''O que deseja fazer?
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] ENCERRAR''')
    opcao = int(input('Qual sua escolha? '))
    if opcao == 1:
        soma = n1 + n2
        print(soma)
    elif opcao == 2:
        res = n1 * n2
        print(res)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(maior)
    elif opcao == 5:
        t = 1
print('END!')