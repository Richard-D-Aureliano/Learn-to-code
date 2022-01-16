nome = str(input('Olá! Primeiramente, nos diga o seu nome: '))
print(f'Prazer em te conhecer {nome}! \nAgora que nos conhecemos melhor')
valor = float(input('Nos diga qual o valor do seu produto: '))

resultado = 'Eba! O seu produto pode entrar no nosso catálogo!' if 20 <= valor <40 else 'Poxa, que pena. Seu produto não atende nossos requisitos'

print (resultado)