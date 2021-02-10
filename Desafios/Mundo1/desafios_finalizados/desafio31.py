# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200Km e R$0,45 para viagens mais longas.

d = int(input('Qual a distância da viagem? Km '))

print(f'- A distância da viagem é de {d}Km.')

if d <= 200:
    # maneira alternativa com objeto:
    preco = d * 0.50
    # maneira utilizando o print:
    # print(f'- O preço da passagem é de R${0.50 * d:.2f}.')
else:
    # maneira alternativa com objeto:
    preco = d * 0.45
    # maneira utilizando o print:
    # print(f'- O preço da passagem é de R${0.45 * d:.2f}.')
print(f'O preço da passagem é de R${preco:.2f}.')
