nt1 = float(input('Digite a primeira nota do aluno: '))
nt2 = float(input('Digite a segunda nota do aluno: '))
nt3 = float(input('Digite a terceira nota do aluno: '))
nt4 = float(input('Digite a quarta nota do aluno: '))
fin = ((nt1 + nt2 + nt3 + nt4) / 4)

print(f'A média final do aluno é {fin}.')
if fin >= 5:
    print('Parabéns! Você foi aprovado!')
else:
    print('Estude um pouco mais!')
