""" 
Задание 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
           (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

Пример:
        k=2 => 2*x**2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x**2 = 0
        k=3 => 2*x**3 + 4*x**2 + 4*x + 5 = 0
"""

from random import randint
from os import getcwd
pathFile = getcwd() + '\\sem_4\\file_4.txt'

def SaveFile(strSave: str):
    with open(pathFile, "a") as fileTxt:
        fileTxt.write(strSave + '\n') 

try:
    inNumK = int(input('Введите значение натуральной степени k='))
    if inNumK > 0:
        strForFile = ''
        temp = 0
        for i in range(inNumK + 1)[::-1]:
            temp = randint(0, 100)
            if temp == 0: continue
            if temp == 1:
                if i > 1: strForFile += 'x**' + str(i) + ' + '
                elif i == 1: strForFile += 'x + '
                else: strForFile += str(temp) + " = 0"
            else: 
                if i > 1: strForFile += str(temp) + '*x**' + str(i) + ' + '
                elif i == 1: strForFile += str(temp) + '*x + '
                else: strForFile += str(temp) + " = 0"
             
        SaveFile(strForFile)    # Запишем полученное в файл
    else: print('Введено некоректное значение.')
    
except ValueError:
    print('Введено некоректное значение.')



