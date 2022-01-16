frase = 'Curso em Vídeo Phyton'

print(frase[3:13])

print(frase[:13])

print(frase[13:])

print(frase[1:15:2])
#Onde começa (início no numero 0);
#Onde termina (no numero anterior ao escrito, ou seja, 14);
#Pulando de quantas em quantas letras;

print(frase[::2])
#Ao deixar vazio, colocamos do início, ao fim, ou sem um inicio definido, ou sem fim definido;

print(frase[1::3])

print('''Nessa aula, vamos aprender operações com String no Python. 
As principais operações que vamos aprender são o Fatiamento de String
Análise com len(), count(), find(), transformações com replace(), upper()
lower(), capitalize(), title(), strip(), junção com join().''')

#Aspas triplas para poder escrever longas sentenças;

print(frase.count('o'))

#Diferença entre maiúsculo e minúsculo;

print(frase.count('O'))

#Colocamos toda a frase em maiúsculo e a contagem muda;

print(frase.upper().count('O'))

print(len(frase))
#Importante para medir o tamanho, conta espaços em branco antes e depois;

frase = '   Curso em Vídeo Python   '

print(len(frase))
#Aqui são somados os espaços em branco;

print(len(frase.strip()))
#Strip corta os espaços em branco desnecessários da sentença;

frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))
print(frase)
#Uma string em seus micro elementos é imutável, a não ser que seja feito:

frase = frase.replace('Python', 'Android')
#Utilização de uma função de troca.
print(frase)

print(frase.find('Curso'))
print(frase.find('Android'))
#Mostra a posição do primeiro caractere; -1 se não existe; diferença entre maiúsculo e minúsculo sempre;
print(frase.lower())
print(frase.lower().find('vídeo'))

print(frase.title())
print(frase.capitalize())

print(frase.split())
dividido = frase.split()
#Vai criar uma lista
print(dividido[0])
print(dividido[2] [3])
