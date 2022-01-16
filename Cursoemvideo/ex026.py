frs = str(input('Digite uma frase: ')).strip()

print(f'Foram encontrados {frs.lower().count("a")} letras A na sua frase.')
print(f'Sendo o primeiro na posição: {frs.lower().find("a")+1}')
print(f'E o último na posição {frs.lower().rfind("a")+1};')

