n1 = int(input('Qual tabuada quer saber? '))
print('--' * 11)
for c in range (1, 11):
    res = c * n1
    print('{} x {} = {}'.format(n1, c, res))
print('--' * 11)