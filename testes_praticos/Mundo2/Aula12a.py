# AULA 12 - CONDIÇÕES ANINHADAS
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# somente if: é chamado de condição simples.
# if + else: é chamado de estrutura condicional composta.
# if + elif + else: é chamado de estrutura condicional aninhada.
# um programa pode funcionar somente com if, ou com if/else, mas não funciona se conter apenas elif/else.

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

nome = str(input('Qual é o seu nome?')).strip()
if nome == 'Raphael':
    print('\033[1;32mQue nome bonito!\033[m')
elif nome == 'José' or nome == 'João' or nome == 'Maria' or nome == 'Raimundo':
    print('\033[1;33mSeu nome é bem popular no Brasil.\033[m')
elif nome in 'Ana Cláudia Joaquina Luiza Joana Paula':
    print('Belo nome feminino.')
else:
    print('\033[1;31mSeu nome é bem normal.\033[m')
print(f'\033[1mTenha um bom dia, {nome}!\033[m')
