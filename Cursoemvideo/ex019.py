from random import choice
al1 = str(input('Escolha o primeiro aluno: '))
al2 = str(input('Escolha o segundo aluno: '))
al3 = str(input('Escolha o terceiro aluno: '))
al4 = str(input('Escolha o quarto aluno: '))
lista = [al1, al2, al3, al4]
res = choice(lista)
print(f'O aluno escolhido foi {res}!')
