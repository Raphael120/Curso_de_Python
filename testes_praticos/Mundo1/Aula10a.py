# AULA 10 - CONDIÇÕES EM PYTHON

# nome = str(input('Qual é o seu nome?'))
# if nome == 'Raphael':
#     print('Que nome bonito você tem!')
# else:
#     print('Seu nome é tão normal!')
# print(f'Bom dia, {nome}!')

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2

print(f'Sua média foi {media}.')
# print('Você foi aprovado.' if media >= 7.0 else 'Você foi reprovado.')
if media >= 7:
    print('Você foi aprovado')
else:
    print('Você foi reprovado')
