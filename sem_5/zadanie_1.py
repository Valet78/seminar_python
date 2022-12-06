""" 
Задание 1. Задано N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
           чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
 1 2 3 4 6 7 -> 5
 1 3 -> 2

"""

def FoundErr(numList: list[int]) -> str:
    ind = len(numList)-1
    while ind > 0:
        if numList[ind] - 1 != numList[ind-1]: return str(numList[ind] - 1 )
        ind -= 1
    return '0'

try:
    inNum = list(map(int, input('Введите последовательность натуральных чисел (через пробел):').split()))
    temp = FoundErr(inNum)
    if temp != '0': print(f'\n{inNum} -> {temp}\n')
    else: print('\nПропущенных чисел не обнаружено.\n')

except ValueError:
    print('Введены некорректные данные.')

