salario_5m = True
nome_limpo = False

if salario_5m or nome_limpo:
    #Se colocar o OR, será aprovado com um verdadeiro no critério
    #And precisa dos dois no critério.
    print('Financiamento aprovado!')
else:
    print('Financiamento negado.')