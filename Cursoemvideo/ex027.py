name = str(input('Digite o seu nome: ')).lower().split()

print('Muito prazer em te conhecer!')
print(f'O seu primeiro nome é {name[0].capitalize()}')
print(f'E o seu último nome é {name[len(name)-1].capitalize()}')
