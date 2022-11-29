""" 
Задание 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
           между максимальным и минимальным значением дробной части элементов.

Пример:
            [1.1, 1.2, 3.1, 5, 10.01] => 0.19

Вариант решения 

"""


#myList = [4.7, 1.8, 1.2, 7.03, 3.1, 5, 10.01]
myList = [1.1, 1.2, 3.1, 5, 10.01]
resList = []
for inn in myList:
    dd = round((inn - int(inn)), 2) * 100
    if dd != 0: resList.append(dd)

res, ttInt  = 0, 0
max, min = int(resList[0]), int(resList[0])
for tt in resList:
    ttInt = int(tt)
    if ttInt < min: min = ttInt
    if ttInt > max: max = ttInt

res = (max - min) / 100

print(f'Разница между максимальным и минимальным значением дробной части элементов списка {myList} равна {res}')
