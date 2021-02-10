# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A".
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.

frase = input('Insira uma frase:').strip()
acount = frase.upper().count("A")
laproc = frase.upper().find("A")+1
raproc = frase.upper().rfind("A", 0)+1
# print(raproc)

print(f'A frase inserida foi: "{frase}".\n'
      f'A letra "A" aparece {acount} vezes.\n'
      f'A letra "A" aparece pela primeira vez na posição {laproc}.\n'
      f'A letra "A" aparece pela última vez na posição {raproc}.\n')

