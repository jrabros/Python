def eleitor(ano_nascimento):
    from datetime import datetime
    idade = datetime.now().year - ano_nascimento
    if idade <= 15:
        print(f'Com {idade} anos. NÃO VOTA')
    elif idade >= 18 and idade <= 60:
        print(f'Com {idade} anos. VOTO OBRIGATÓRIO')
    else:
        print(f'Com {idade} anos. VOTO OPICIONAL')

nasc = int(input(('Em que ano você nasceu? ')))
eleitor(nasc)