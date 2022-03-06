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