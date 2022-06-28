# importação relativa de módulos nativos do Python
from math import sqrt, factorial
from random import randint

# importação relativa de um arquivo no mesmo diretório do programa
from exercicio04 import intercala_numeros


n = sqrt(100)
print(n)

n = factorial(5)
print(n)

n = randint(1, 100)
print(n)

n = intercala_numeros([1, 2, 3], [5, 6, 7])
print(n)
