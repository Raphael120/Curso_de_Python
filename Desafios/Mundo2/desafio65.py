"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores."""

# SEM PONTO DE PARARDA (COM 'BREAK')

num = 0
soma = 0
media = 0
maior = []
menor = []
contagem = 0

while num >= 0:
    num = int(input("Digite um número inteiro: "))
    if num >= 0:
        contagem += 1
        soma += num
        media = soma / contagem
        maior += [num]
        menor += [num]
        if num >= 0:
            print(':::' * 30)
            opcao = str(input('Você quer digitar outros valores? [S / N] ')).upper().strip()
            print(':::' * 30)
            if opcao == 'S':
                continue
            else:
                print('VOCÊ OPTOU POR FINALIZAR O PROGRAMA.\n'
                      f'- Média dos valores digitados: {media:.1f}.\n'
                      f'- Maior valor digitado: {max(maior)}.\n'
                      f'- Menor valor digitado: {min(menor)}.')
                break


# COM PONTO DE PARADA 999(FLAG):
"""num = 0
soma = 0
media = 0
maior = []
menor = []
contagem = 0
while num != 999:
    num = int(input("Digite um número inteiro (Digite '999' para parar o programa): "))
    if num != 999:
        contagem += 1
        soma += num
        media = soma / contagem
        maior += [num]
        menor += [num]
        if num != 999:
            opcao = str(input('Você quer digitar outros valores? [S / N] ')).upper().strip()
            if opcao == 'S':
                continue
            else:
                print('VOCÊ OPTOU POR FINALIZAR O PROGRAMA.\n'
                      f'Média: {media:.1f}\n'
                      f'Maior: {max(maior)}\n'
                      f'Menor: {min(menor)}')
                break
else:
    print(f'Média: {media:.1f}\n'
          f'Maior: {max(maior)}\n'
          f'Menor: {min(menor)}')"""
