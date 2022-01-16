print('Tabela de reajuste salarial')
nome = input('Olá funcionário, por favor diga o seu nome: ')
sal = float(input('Agora, nos diga qual é o seu salário: '))
reajuste = sal*0.15
print(f'Obrigado por aguardar {nome:*^20}. Com base nos cálculos, o seu salário de {sal} irá para {reajuste+sal:.2f}!')
print('!!Parabéns!!')