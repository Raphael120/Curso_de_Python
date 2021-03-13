# Escreva um programa que leia a velocidade de um carro.
# - Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# - A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Qual a velocidade do carro: Km/h '))
print('-<>-' * 25)
print('- Se o veículo ultrapassar os 80Km/h, será aplicada uma multa de R$7,00 por cada Km acima do limite.')
print('-<>-' * 25)

if vel <= 80:
    print(f'- A velocidade do veículo é de {vel}Km/h.\n'
          '- A velocidade está dentro do permitido.')
else:
    print('- Você excedeu a velocidade permitida e por isso será multado!\n'
          f'- Sua multa será de R${(vel - 80) * 7:.2f}.')
