lista = [7,8,9,5,1,2,2,3,4,5]
num = len(lista)
lista.sort()
  
if num % 2 == 0:
    medianaNum1 = lista[num//2]
    medianaNum2 = lista[num//2 - 1]
    mediana = (medianaNum1 + medianaNum2)/2
else:
    mediana = lista[num//2]
print("A mediana é: " + str(mediana))