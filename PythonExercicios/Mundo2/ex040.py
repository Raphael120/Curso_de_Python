# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida:
# - Média abaixo de 5.0: "REPROVADO"
# - Média entre 5.0 e 6.9: "RECUPERAÇÃO"
# Média 7.0 ou superior: "APROVADO"

from time import sleep

print('\033[1;36mCALCULADORA DE MÉDIA ESCOLAR\033[m\n')
sleep(1)
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota:'))
media = (nota1 + nota2) / 2
sleep(1)
print(f'A sua primeira nota foi \033[1;32m{nota1}\033[m e a segunda nota \033[1;32m{nota2}\033[m.\n')
if media < 5.0:
    print(f'Sua média foi de \033[1;32m{media:.1f}\033[m\n'
          f'Você foi \033[1;31mREPROVADO\033[m.')
elif media >= 7.0:
    print(f'Sua média foi de \033[1m{media:.1f}\033[m\nVocê foi \033[1;32mAPROVADO\033[m.\n'
          f'\033[1;34mParabéns!!!\033[m')
else:
    print(f'Sua média foi de \033[1m{media:.1f}\033[m\n'
          f'Você está de \033[1;33mRECUPERAÇÃO\033[m.')
