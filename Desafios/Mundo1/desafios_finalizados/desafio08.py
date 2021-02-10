# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = (float(input('Insira um valor em metros:')))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(
    f'O valor inserido foi {m} metros.\n'
    f'{m} metros é equivalente a {km} quilômetros.\n'
    f'{m} metros é equivalente a {hm} hectômetros.\n'
    f'{m} metros é equivalente a {dam} decâmetros.\n'
    f'{m} metros é equivalente a {dm} decímetros.\n'
    f'{m} metros é equivalente a {cm} centímetros.\n'
    f'{m} metros é equivalente a {mm} milímetros.'
)
print('==================================================')
# ou
# print(f'O valor inserido foi {m} metros.')
# print(f'{m} metros é equivalente a {m * 100} centímetros.')
# print(f'{m} metros é equivalente a {m * 1000} milímetros.')
