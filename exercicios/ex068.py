import random
lista = ('Pedra', 'Papel', 'Tesoura')
while True:
    print('''
Vamos jogar!
Escolha um:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
    ''')
    computador = random.randint(0,2)
    jogador = int(input('Qual opção você escolhe? '))
    if lista[computador] == 'Pedra':
        if jogador == 1:
            print(f'Computador escolheu {lista[0]} -> EMPATOU')
        elif jogador == 2:
            print(f'Computador escolheu {lista[0]} -> JOGADOR VENCEU')
            break
        else:
            print(f'(Computador escolheu {lista[0]}) -> COMPUTADOR VENCEU')
    if lista[computador] == 'Papel':
        if jogador == 1:
            print(f'Computador escolheu {lista[1]} -> COMPUTADOR VENCEU')
        elif jogador == 2:
            print(f'Computador escolheu {lista[1]} -> EMPATOU')
        else:
            print(f'Computador escolheu {lista[1]} -> JOGADOR VENCEU')
            break
    if lista[computador] == 'Tesoura':
        if jogador == 1:
            print(f'Computador escolheu {lista[2]} -> JOGADOR VENCEU')
            break
        elif jogador == 2:
            print(f'Computador escolheu {lista[2]} -> COMPUTADOR VENCEU')
        else:
            print(f'Computador escolheu {lista[2]} -> EMPATOU')