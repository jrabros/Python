i = soma = qtd = 0
while i == 0:
    n1 = int(input('Digite um número: '))
    print('Se quiser cancelar operação digite 999')
    if n1 == 999:
        i = 1
    else:
        soma += n1
        qtd += 1
print('soma é {} e foi digitado {} vezes'.format(soma, qtd))