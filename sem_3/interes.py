# Заполнение списка из N элементов
from math import factorial
n = 6

# 1. вариант
# mult = [factorial(i) for i in range(1, n+1)]

# 2. вариант
mult = []
for i in range(1, n+1):
    mult.append(factorial(i)) 

print(f'\n{mult} \n')

