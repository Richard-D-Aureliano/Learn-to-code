'''ops = float(input('Qual o comprimento do cateto oposto? '))
adj = float(input('Qual o comprimento do cateto adjacente? '))
hip = (ops ** 2 + adj ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hip:.2f}.')'''

from math import hypot
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hip = hypot(co, ca)
print(f'A hipotenusa vai medir {hip:.2f}.')
