dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
total = dia * 60 + km * 0.15
print(f'O total a pagar por {dia} dias e {km}km rodados é de R${total:.2f}.')
