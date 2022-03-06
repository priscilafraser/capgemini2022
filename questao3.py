import math

texto = input("Digite o texto: ")
texto = texto.replace(" ", "")
print(texto)
len(texto)

raiz = len(texto)**0.5
print(raiz)

print(f'Grid será de {math.ceil(raiz)}')