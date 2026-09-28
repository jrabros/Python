jogador = dict()
partidas = list()
jogadores = list()
while True:
    jogador['nome'] = str(input('Qual o nome do jogador? '))
    jogador['partidas'] = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    for c in range(0, jogador['partidas']):
        partidas.append(int(input(f'Quantos gols fez na partida {c}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    jogadores.append(jogador.copy())
    partidas.clear()
    resp = str(input('Quer continuar? [S/N]' ))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()