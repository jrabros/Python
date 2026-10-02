def fatorial(n, show=False):
    f = 1
    for c in range (n, 0, -1):
        if show == True:
            f *= c
            print(f'{c}', end=' x ' if c > 1 else ' = ')
        else:
            f *= c
    print(f)            


fatorial(9, True)