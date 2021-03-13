# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número:'))
dobro = n * 2
triplo = n * 3
raiz = n ** 0.5

print(f'- O dobro do número {n} é {dobro}.\n- O triplo do número {n} é {triplo}.\n- A raiz quadrada do número {n} é {raiz:.1f}.')
# ou
print(f'O dobro do  número {n} é {n * 2}.\n- O triplo do número {n} é {n * 3}. \n- A raiz quadrada do número {n} é {n ** 0.5:.1f}.')
