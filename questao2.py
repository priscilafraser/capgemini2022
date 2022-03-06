el = int(input('Digite a quantidade de elementos: '))

vet = list()
for i in range(1, el + 1):
    while True:
        try:
            v = int(input(f'Digite o {i}º valor: '))
            break
        except ValueError:
            print('Valor INVÁLIDO! Digite apenas valores inteiros!')
    vet.append(v)
    
print(f'A lista de números digitados foi:\n{vet}')

ls = vet
pares = []
cont =0
resultado= []
diferenca = int(input("Digite o valor da diferença desejada: "))

print("Os pares encontrados com a diferença especificada foram:")
for i in vet:
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
