soma_idade = 0
idade_older = 0
qnt = 0
older = ''
for c in range (1,5):
    nome = str(input('Digite o nome da pessoa '))
    idade = int(input('Qual a idade da pessoa '))
    sexo = str(input('Qual o Sexo da pessoa? [M] ou [F]'))
    soma_idade += idade
    if sexo in "Mm":
        if idade > idade_older:
            idade_older = idade
            older = nome
    else:
        if idade < 20:
            qnt +=1
media = soma_idade/4
print('A media de idade de todos os registrado é de {}'.format(media))
if older != '': 
    print('O homem mais velho é {}'.format(older))
else:
    print('Não ha homens registrados')
if qnt > 0:
    print('Há {} mulheres com menos de 20 anos'. format(qnt))
else:
    print('Não há mulheres com menos de 20 anos')
