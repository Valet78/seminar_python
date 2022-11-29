""" 
Задание 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
           между максимальным и минимальным значением дробной части элементов.

Пример:
            [1.1, 1.2, 3.1, 5, 10.01] => 0.19

"""


#myList = [4.7, 1.8, 1.2, 7.03, 3.1, 5, 10.01]
myList = [1.1, 1.2, 3.1, 5, 10.01]
resList = []
for inn in myList:
    innTxt = str(float(inn))
    indPoint = innTxt.find('.') + 1         # находим координаты цифры за точкой
    dd = innTxt[indPoint:indPoint + 2]      # готовим подстроку
    if len(dd) == 1: dd += '0'
    if dd != '00': resList.append(dd)

res, ttInt  = 0, 0
max, min = int(resList[0]), int(resList[0])
for tt in resList:
    ttInt = int(tt)
    if ttInt < min: min = ttInt
    if ttInt > max: max = ttInt
print(f'max = {max}, min = {min}\n')
res = (max - min) / 100
#res = '0.' + str(max - min)

print(f'Разница между максимальным и минимальным значением дробной части элементов списка {myList} равна {res}')