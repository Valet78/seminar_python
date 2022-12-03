""" 
Задание 3. Задайте последовательность чисел. Напишите программу, которая 
           выведет список неповторяющихся элементов исходной последовательности.
"""

from random import randint

myList = [randint(1, 49) for i in range(20)]
print(f'\n{myList}')
print(f'{[res for res in myList if myList.count(res) == 1]} \n')