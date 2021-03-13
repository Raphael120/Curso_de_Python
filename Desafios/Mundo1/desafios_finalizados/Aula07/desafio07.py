# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

nome = str(input('Digite o nome do aluno:'))
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2

print(f'a média do(a) aluno(a) {nome} foi: {m:.1f}. ')

if m >= 7.0:
    print('Situação: Aprovado.')
elif m >= 5.0:
    print('Situação: Recuperação.')
else:
    print('Situação: Reprovado.')
