# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Insira o nome da pessoa:')
upnome = nome.upper().split()
procnome = upnome.count('SILVA')

print(f'O nome inserido foi {nome}. '
      f'O(A) {nome} tem "SILVA" no nome?\n'
      f'===========================================================\n'
      f'Caso a resposta for "Sim", o programa retornará o número 1.\n'
      f'Caso a resposta for "Não", o programa retornará o número 0.\n'
      f'===========================================================\n'
      f'A resposta é : {procnome}.')

nome1 = str(input('Insira o nome da pessoa:')).strip()
nome2 = 'SILVA' in nome1.upper().split()
print(f'O nome inserido foi {nome1}.\n'
      f'{nome1} tem "Silva" no nome? {nome2}')