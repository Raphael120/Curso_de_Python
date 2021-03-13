# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Insira o nome de uma cidade:')
busca = cidade.upper().split()
inicial = busca[0].count("SANTO")

print(f'A cidade é {cidade.upper()}. '
      f'A cidade começa com o nome "SANTO"?\n'
      f'-------------------------------------------------------------\n'
      f'Caso a resposta for "Sim", o programa retornará o número 1\n'
      f'Caso a resposta for "Não", o programa retornará o número 0\n'
      f'-------------------------------------------------------------\n'
      f' o resultado é: "{inicial}".')

cidade1 = str(input('Insira o nome de uma cidade:')).strip()
cid = cidade1[:5].upper() == 'SANTO'
print(f'A cidade ´´e {cidade1}.\n'
      f'A cidade começa com o nome "SANTO"?\n'
      f'{cid}')
