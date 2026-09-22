fatorial = 1
n = int(input('Digite um número: '))
s = n
while n > 1:
    fatorial = fatorial * n
    n -= 1
print('O fatorial de {}! é {}'.format(s, fatorial))