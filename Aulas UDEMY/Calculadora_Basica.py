def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print('Selecione a operação:')
print('1: Adição;')
print('2: Subtração;')
print('3: Multiplicação;')
print('4: Divisão;')

while True:
    choise = input('Selecione a operação desejada (1, 2, 3, 4): ')

    if choise in ('1', '2', '3', '4'):
        num1 = float(input('Escolha o primeiro número: '))
        num2 = float(input('Escolha o segundo número: '))

        if choise == '1':
            print(f'{num1} + {num2} = {num1 + num2}.')
        elif choise == '2':
            print(f'{num1} - {num2} = {num1 - num2}.')
        elif choise == '3':
            print(f'{num1} * {num2} = {num1 * num2}.')
        elif choise == '4':
            print(f'{num1} / {num2} = {num1 / num2}.')
        break
    else:
        print('Erro')
