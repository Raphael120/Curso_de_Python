"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores."""

num = 0
soma = 0
media = 0
maior = 0
menor = 0
contagem = 0
while num != 999:
    num = int(input("Digite um número inteiro (Digite '999' para parar o programa): "))
    if num != 999:
        contagem += 1
        soma += num
        media = soma / contagem
        maior = num
        menor = num
        
else:
    print(f'Média: {media:.1f}\n')
          # f'Maior: {max(num)}')
    # maior, menor)