# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('\033[1mDigite um número:\033[m'))

n0 = n1 - 1
n2 = n1 + 1

print(f'O número digitado foi \033[1;33m{n1}\033[m. Seu antecessor é o número \033[1;31m{n0}\033[m '
      f'e seu sucessor é o número \033[1;34m{n2}\033[m.')
# ou
print(f'O número digitado foi \033[1;33m{n1}\033[m. Seu antecessor é o número \033[1;31m{n1 - 1}\033[m '
      f'e seu sucessor é o número \033[1;34m{n1 + 1}\033[m.')
