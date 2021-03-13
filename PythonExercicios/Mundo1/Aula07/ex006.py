# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('\033[1;41mDigite um número:\033[m'))
dobro = n * 2
triplo = n * 3
raiz = n ** 0.5

print(f'- O dobro do número \033[1;32m{n}\033[m é \033[1;36m{dobro}\033[m.\n'
      f'- O triplo do número \033[1;32m{n}\033[m é \033[1;36m{triplo}\033[m.\n'
      f'- A raiz quadrada do número \033[1;32m{n}\033[m é \033[1;36m{raiz:.1f}\033[m.')
# ou
print(f'O dobro do  número \033[1;32m{n}\033[m é \033[1;36m{n * 2}\033[m.\n'
      f'- O triplo do número \033[1;32m{n}\033[m é \033[1;36m{n * 3}\033[m. \n'
      f'- A raiz quadrada do número \033[1;32m{n}\033[m é \033[1;36m{n ** 0.5:.1f}\033[m.')
