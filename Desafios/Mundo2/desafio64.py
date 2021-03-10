"""Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)"""

# COM FLAG (PONTO DE PARADA):
'''f = 999
num = int(input('Insira um número inteiro (Digite "999" para parar a sequência): '))
while f != num:
    num += 1
    print(num)'''

num = 0
soma = 0
contagem = 0

# while True:
while num >= 0:
    num = int(input("Digite um número inteiro (Digite '999' para parar o programa): "))
    # while num != 999:
    #     num += 1
    #     print(num)
    # else:
    #     print('VOCÊ OPTOU POR FINALIZAR O PROGRAMA.')
    #     break
    if num != 999:
        soma += num
        contagem += 1
        # print(soma, contagem)
    else:
        print('VOCÊ OPTOU POR PARAR O PROGRAMA.')
        break
else:
    print(f'Foram digitados {contagem} números. A soma entre eles é: {soma}.')
