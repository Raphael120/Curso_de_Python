# AULA 7 - OPERADORES ARITMÉTICOS

# nome = input('Qual é o seu nome?')

# print(f'Prazer em conhece-lo,{nome:=^20}!')
# print(f'Prazer em conhece-lo,{nome:<20}!')
# print(f'Prazer em conhece-lo,{nome:>20}!')

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print(f'A soma é {s}, a multiplicação é {m} e a divisão é {d:.3f}.', end=' >>> ')
print(f'a Divisão inteira é {di} e a potencia é {p}.')

# "\n" : quebra de linha no print.
# "end=''" : "junta" dois prints numa mesma linha.
