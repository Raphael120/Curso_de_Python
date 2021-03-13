# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a quantidade de Km percorridos:'))
dias = float(input('Digite a quantidade de dias em que o carro foi alugado:'))
preco = dias * 60
rodagem = km * 0.15

print(f'- O carro percorreu {km} Quilômetros e foi alugado por {dias} dias.\n'
      f'- O preço a pagar pelo aluguel do carro é de R${preco:.2f} pelos dias em que '
      f'permaneceu alugado e R${rodagem:.2f} pelos Quilômetros rodados.\n'
      f'- O valor total a ser pago pelo aluguel do veículo é de R${preco + rodagem:.2f}.')
