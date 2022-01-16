eleitor = int(input('Qual a idade do eleitor? '))

'''if eleitor >= 16:
    resultado = print('Está liberado para votar!')
else:
    resultado = print('Quem sabe no próximo ano.')'''

resultado = 'Está liberado para votar' if eleitor >= 16 else 'Quem sabe no próximo ano'

print(resultado)
