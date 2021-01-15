# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles. (Usar emoji de foguete)

from emoji import emojize
from time import sleep


print('Contagem regressiva para o Ano-Novo!!!')
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
sleep(1)
print('\033[1;34mFeliz 2021!!!!!!\033[m ')
print(emojize(':fireworks:' * 40, use_aliases=True))
