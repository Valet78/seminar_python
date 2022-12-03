""" 
Задание 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

Пример:
        6   -> [1,2,3]
        144 -> [2,3]

"""
from sympy import primefactors

def SpisokRealOne(num: int):
    listRes = []
    temp, st = num, 0
    for ind in [2, 3, 5, 7]:        
        while temp % ind == 0: 
            temp /= ind
            st += 1        
        if st > 0: 
            listRes.append(ind)
            temp, st = int(num / (ind**st)), 0 
    if temp != 0: listRes.append(temp)
    return listRes


try:
    inNum = int(input('Введите натуральное число N: '))
    if inNum != 0:
        print('\nВариант 1:')
        print(f'\tДля N = {inNum} -> {SpisokRealOne(inNum)}')
        print('\nВариант 2:')
        print(f'\tДля N = {inNum} -> {primefactors(inNum)}\n')       
        
        
    else: print('Введенно некорректное значение.')
except:
    print('Введенно некорректное значение.')



