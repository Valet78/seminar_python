""" 
Задание 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

Пример:
        4, 5 -> 20
        4, 6 -> 12
"""

from math import gcd

def NokOne(inA: int, inB: int) -> int:
    return (inA * inB) // gcd(inA, inB)
    
def NokTwo(inA: int, inB: int) -> int:
    if inA > inB: max = inA
    else: max = inB
    while(True): 
        if((max % inA == 0) and (max % inB == 0)): 
            temp = max 
            break 
        max += 1 
    return temp 


try:
    inNum = list(map(int, input('Введите через пробел два числа A и B для нахождения НОК (A≠0 и B≠0): ').split()))
    numA, numB = inNum
    if numA !=0 and numB != 0:
        print('Вариант 1:')
        print(f'\tНаименьшее общее кратное для чисел {numA} и {numB} -> {NokOne(numA, numB)}\n')

        print('Вариант 2:')
        print(f'\tНаименьшее общее кратное для чисел {numA} и {numB} -> {NokTwo(numA, numB)}\n')
    else: print('Числа А и В не соответствуют условиям A≠0 и B≠0!')
    
except ValueError: print('Введены некорректные данные!')




