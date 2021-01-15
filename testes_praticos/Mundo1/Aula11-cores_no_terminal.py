
# CÓDIGO PARA COR:
# \033['style';'text';'background'm
# ex: \033[0;33;44m
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# STYLE:
# 0(none),                  4(sublinhado),
# 1(bold = negrito),        7(negative = inverte as cores)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# TEXT: todas começam com número 3, sendo do número 30 a 37:
# 30:branco,               34:azul,
# 31:vermelho,              35:roxo,
# 32:verde,                 36:ciano,
# 33:amarelo,               37:cinza.

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# BACKGROUND: cores de fundo. Começam com número 4, sendo do número 40 a 47 e com o mesma sequencia de cores do texto.

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
print('\033[;31mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')
print('\033[7;33;44mOlá, Mundo!\033[m')
a = 3
b = 5
nome = 'Raphael'
cores = {"limpa": '\033[m',
         "azul": '\033[34m',
         "amarelo": '\033[33m',
         "pretoebranco": '\033[7;30m'}

print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m.')
print(f'Olá, prazer em conhece-lo, \033[4;34m{nome}\033[m!')
print(f'Olá, prazer em conhece-lo,{cores["pretoebranco"]}{nome}{cores["limpa"]}!')

