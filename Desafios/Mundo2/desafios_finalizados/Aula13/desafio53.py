# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex: 'APOS A SOPA', 'A SACADA DA CASA', 'A TORRE DA DERROTA', 'O LOBO AMA O BOLO', 'ANOTARAM A DATA DA MARATONA'.

frase = str(input('Insira uma frase:')).upper().strip().replace(' ', '')

for i in frase:
    if frase == frase[::-1]:
        print('A frase inserida é um Palíndromo.')
        break
else:
    print('A frase inserida não é um Palíndromo.')
