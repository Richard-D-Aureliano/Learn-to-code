from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
coseno = cos(radians(an))
tangente = tan(radians(an))
print(f'O ângulo de {an} tem o SENO de {seno:.2f}.')
print(f'O ângulo de {an} em o COSENO de {coseno:.2f}.')
print(f'O ângulo de {an} em a sua TANGENTE de {tangente:.2f}.')
