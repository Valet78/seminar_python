""" 
Задание 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

Пример:
        6   -> [1,2,3]
        144 -> [2,3]

"""
from sympy import primefactors

def SpisokRealOne(num: int):
    listRes = []
    temp, st = num, 2
    while temp != 1:        
        while temp % st == 0: 
            temp //= st
            listRes.append(st)
        st += 1              
    return sorted(list(set(listRes))) 

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



