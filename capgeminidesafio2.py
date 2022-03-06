# QUESTAO 1

lista = [7,8,9,5,1,2,2,3,4,5]
num = len(lista)
lista.sort()
  
if num % 2 == 0:
    medianaNum1 = lista[num//2]
    medianaNum2 = lista[num//2 - 1]
    mediana = (medianaNum1 + medianaNum2)/2
else:
    mediana = lista[num//2]
print("Median is: " + str(mediana))

# Questão 2

l = [1, 5, 3, 4, 2]
ls = [1, 5, 3, 4, 2]

pares = []
cont =0
resultado= []
diferenca = int(input())

print("Os pares encontrados com a diferença especificada foram:")
for i in l:
  for j in ls:
    menos = abs(i - j)
    pares.append(menos)
    if menos == diferenca:
      print(f'|{i}-{j}|')
      resultado.append([i,j])
      cont += 1

if cont == 0:
  print('Diferença não encontrada')

print(f'O total de pares não repetidos são {cont/2}')

# Questão 3

import math

texto = input("Digite o texto: ")
texto = texto.replace(" ", "")
print(texto)
len(texto)

raiz = len(texto)**0.5
print(raiz)

print(f'Grid será de {math.ceil(raiz)}')