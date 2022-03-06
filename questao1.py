m = int(input('Digite a quantidade de elementos: '))

lista = list()
linha = list()
for i in range(1, m + 1):
    while True:
        try:
            v = int(input(f'Digite o {i}º valor: '))
            break
        except ValueError:
            print('Valor INVÁLIDO! Digite apenas valores inteiros!')
    linha.append(v)
    lista.append(linha)
print(f'A lista de números digitados foi:\n{linha}')

num = len(linha)
linha.sort()
  
if num % 2 == 0:
    medianaNum1 = linha[num//2]
    medianaNum2 = linha[num//2 - 1]
    mediana = (medianaNum1 + medianaNum2)/2
else:
    mediana = linha[num//2]
print("A mediana é: " + str(mediana))
