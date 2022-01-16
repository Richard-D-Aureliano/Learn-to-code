velocidade = float(input('Qual a velocidade do veículo? '))

if velocidade > 110:
    print('Acima da velocidade permitida.')
    print('Favor, reduzir a sua velocidade.')
elif velocidade < 80:
    print('Velocidade muito a baixo do normal.')
    print('Aumente a velocidade.')
else:
    print('Velocidade OK.')