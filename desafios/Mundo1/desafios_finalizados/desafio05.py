# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um número:'))

n0 = n1 - 1
n2 = n1 + 1

print(f'O número digitado foi {n1}. Seu antecessor é o número {n0} e seu sucessor é o número {n2}.')
# ou
print(f'O número digitado foi {n1}. Seu antecessor é o número {n1 - 1} e seu sucessor é o número {n1 + 1}.')
