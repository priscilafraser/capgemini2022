# Capgemini - Desafio 2

>Questões referentes ao DESAFIO DE PROGRAMAÇÃO 02 - ACADEMIA CAPGEMINI.

Terceira etapa do processo, tem como objetivo testar os conhecimentos em lógica de programação dos candidatos.

## Questões

Desafio respondido em Python com menor uso possível de bibliotecas que facilitassem a resolução. Os códigos rodam apenas no terminal através de inputs (comandos) no teclado. Com frases que indicam as informações e formato que devem ter como entrada.

## Questão 1

*A mediana de uma lista de números é basicamente o elemento que se encontra no meio da lista após a ordenação. Dada uma lista de números com um número ímpar de elementos, desenvolva um algoritmo que encontre a mediana.*

Aqui, foi feito um algoritmo simples do cálculo da mediana. Com os dados de entrada (lista) sendo fornecidos pelo usuário.

## Questão 2

*Dado um vetor de inteiros n e um inteiro qualquer x. Construa um algoritmo que determine o número de elementos pares do vetor que tem uma diferença igual ao valor de x.*

Nesta questão, foi feito um algoritmo em que foi duplicada a lista fornecida pelo usuário, onde pode-se fazer o cálculo da diferença entre os elementos. A diferença entre os elementos também é fornecida pelo usuário, dessa forma, aparecem todos os pares que obtiveram este valor. Como saída tem-se a quantidade de pares com números não repetidos.

## Questão 3

*Um texto precisa ser encriptado usando o seguinte esquema. Primeiro, os espaços são removidos do texto. Então, os caracteres são escritos em um grid, no qual as linhas e colunas tem as seguintes regras:

                raiz(T)<=linha<=coluna<=raiz(T)

Considere T, como o tamanho do texto.
Se certifique de que linhas x colunas >= .
Se múltiplos grids satisfazem as condições, escolha aquele com a menor área.
Escreva um algoritmo que ao receber uma string s, mostre a mensagem encriptada de acordo com as regras descritas.*

Nesta questão foi feito a retirada de espaços, o cálculo da raiz quadrada da quantidade de caracteres, do grid e o primeiro fatiamento de acordo com este grid.
