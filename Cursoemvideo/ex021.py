from random import shuffle

al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al03 = str(input('Terceiro aluno: '))
al04 = str(input('Quarto aluno: '))
lista = [al1, al2, al03, al04]
shuffle(lista)
print(f'A ordem de apresentação será {lista}!')
