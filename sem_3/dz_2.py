""" 
Задание 2. Напишите программу, которая найдёт произведение пар чисел списка. 
           Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:
 [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
 [2, 3, 5, 6] => [12,15]           ( [2*6, 3*5]) 
В скобках пример, как это работает!!!

"""

from random import randint

n = 9          # количество элементов списка myList
myList = [randint(1, 9) for i in range(n)]
resList = []

if n % 2 == 0: indRes = int(n / 2)    
else: indRes = int(n / 2) + 1

for i in range(indRes):
    resList.append(myList[i] * myList[(n - 1) - i])
    
print(f'\nДля списка {myList} произведение пар чисел => {resList}\n')
