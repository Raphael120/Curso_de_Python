# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².


lar = float(input('Digite a largura em metros:'))
alt = float(input('Digite a altura em metros:'))
area = lar * alt
tinta = area / 2

print(f'A parede tem dimensão de {lar} x {alt} e possui uma área de {area:.2f} m².'
      f' Para pintá-la, será necessário {tinta:.1f} litros de tinta.')
