# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = (float(input('\033[7;30mInsira um valor em metros:\033[m')))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(
    f'O valor inserido foi {m} metros.\n'
    f'\033[1;32m{m}\033[m metros é equivalente a \033[1;35m{km}\033[m quilômetros.\n'
    f'\033[1;32m{m}\033[m metros é equivalente a \033[1;35m{hm}\033[m hectômetros.\n'
    f'\033[1;32m{m}\033[m metros é equivalente a \033[1;35m{dam}\033[m decâmetros.\n'
    f'\033[1;32m{m}\033[m metros é equivalente a \033[1;35m{dm}\033[m decímetros.\n'
    f'\033[1;32m{m}\033[m metros é equivalente a \033[1;35m{cm}\033[m centímetros.\n'
    f'\033[1;32m{m}\033[m metros é equivalente a \033[1;35m{mm}\033[m milímetros.'
)
print('===' * 25)
# ou
# print(f'O valor inserido foi {m} metros.')
# print(f'{m} metros é equivalente a {m * 100} centímetros.')
# print(f'{m} metros é equivalente a {m * 1000} milímetros.')
