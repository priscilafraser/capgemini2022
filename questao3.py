import math

texto = input("Digite o texto: ").replace(" ", "")

raiz = len(texto)**0.5
print(f'A raiz é {raiz}')

arredondamento = math.ceil(raiz)
print(f'O grid será de {arredondamento}')

fatiamento = texto.split(texto[arredondamento])
print(fatiamento)

for i in fatiamento:
    print(i)