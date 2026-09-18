n1 = int(input('Qual a valor da tabuada você quer? '))
i = 0
print('_' * 12)
while i <= 10:
    res = n1 * i
    print('{} x {} = {}'.format(n1, i, res))
    i += 1
print('_' * 12)
