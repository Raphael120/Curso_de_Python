
nome = str(input('Insira seu nome: '))
numero = int(input('Insira seu número de identificação: '))
horas = int(input('Insira a quantidade de horas trabalhadas: '))
valor = float(input('Insira o valor da hora trabalhada: R$'))

print(f'\nSeu nome é {nome} e seu número de identificação é: {numero}\n'
      f'Quantidade de horas trabalhadas = {horas} horas\n'
      f'Valor da hora trabalhada = R$ {valor:.2f}\n'
      f'Seu salário é de = R$ {horas * valor:.2f}\n')
