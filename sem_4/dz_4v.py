""" 
Задание 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
           (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

Пример:
        k=2 => 2*x**2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x**2 = 0
        k=3 => 2*x**3 + 4*x**2 + 4*x + 5 = 0

        Версия с использованием sympy
"""

from random import randint
from sympy import simplify
from os import getcwd
pathFile = getcwd() + '\\sem_4\\file_4.txt'

def SaveFile(strSave: str):
    
    with open(pathFile, "a") as fileTxt:
        fileTxt.write(strSave + '\n') 


def GenPolinom(k: int) -> str:
    temp = ''
    for i in range(k + 1)[::-1]:
        if i > 0: temp += f'{randint(0, 100)}*x**{i} + ' 
        else: temp += f'{randint(0, 100)}*x**{i}'
    temp = str(simplify(temp)) + ' = 0'
    return temp

try:
    inNumK = int(input('Введите значение натуральной степени k='))
    if inNumK > 0:
        #strForFile = str(simplify(GenPolinom(inNumK))) 
        strForFile = GenPolinom(inNumK)       
        SaveFile(strForFile)    # Запишем полученное в файл
    else: print('Введено некоректное значение.')
    
except ValueError:
    print('Введено некоректное значение.')



