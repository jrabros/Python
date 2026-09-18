valor = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(valor),
      '\nÉ um valor alfabético?', valor.isalpha(),
      '\nÉ um valor numérico?', valor.isnumeric(),
      '\nÉ um valor em maiúsculo?', valor.isupper(),
      '\nÉ um valor em minúsculo?', valor.islower(),
      '\nÉ um valor alfanumérico?', valor.isalnum(),
      '\nÉ uma valor decimal?',valor.isdecimal(),
      )