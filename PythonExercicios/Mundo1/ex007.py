# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

nome = str(input('\033[1;34mDigite o nome do aluno:'))
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:\033[m'))
m = (n1 + n2) / 2

print(f'a média do(a) aluno(a) \033[1;32m{nome}\033[m foi: \033[1;36m{m:.1f}\033[m. ')

if m >= 7.0:
    print('Situação: \033[1;32mAprovado\033[m.')
elif m >= 5.0:
    print('Situação: \033[1;33mRecuperação\033[m.')
else:
    print('Situação: \033[1;31mReprovado\033[m.')
