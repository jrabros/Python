# n1 = 0
# while n1 == 0:
#     sexo = str(input('Qual o sexo da pessoa? [F/M]')).upper()
#     if sexo == 'M' or sexo == 'F':
#         n1 = 1
#     else:
#         print('Digitou errado, tente novamente')
#         n1 = 0

# alternativa de resposta
sexo = str(input('Informe o sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input(('Dados inválidos, tente novamente '))).strip().upper()[0]
print('Sexo {} cadastro com sucesso'.format(sexo))