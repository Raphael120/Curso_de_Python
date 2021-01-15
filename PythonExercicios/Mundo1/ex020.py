# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle as sorteio

a1 = input('Digite o nome do primeiro aluno:')
a2 = input('Digite o nome do segundo aluno:')
a3 = input('Digite o nome do terceiro aluno:')
a4 = input('Digite o nome do quarto aluno:')
alunos = [a1, a2, a3, a4]
sorteio(alunos)
print(f'A ordem de apresentação do trabalho será a seguinte :\n{alunos}')


