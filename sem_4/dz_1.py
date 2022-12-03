""" 
Задание 1. Вычислить число Пи c заданной точностью d

Пример:
    при d = 0.001, π = 3.141
    при d = 0.0001, π = 3.1415  

"""
from math import pi
try:
    inNum = input('Введите значение точности вывода числа Пи (например: 0.001): ').replace(',', '.')
    if inNum != '':
        number = pi
        inNumTxt = inNum.split('.')[1]    
        lenDrob = str(len(inNumTxt))
        text = '\nДля указанной точности 10^(-' + lenDrob + ') PI = {:.' + lenDrob + 'f}\n'
        print(text.format(number))
    else: print('Введенно некорректное значение.')
except:
    print('Введенно некорректное значение.')