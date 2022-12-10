'''
Задание 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

'''
""" 
inNumTxt = input('Введите количество элементов набора произведений N = ')
if inNumTxt.isnumeric():
    listNum = [1]
    inNum = int(inNumTxt)
    for i in range(1, inNum):
        listNum.append(listNum[i-1] * (i + 1))

    
    print(f'Для N = {inNum} набор произведений {listNum}')
else: print('Введённая последовательность символов не является натуральным числом.')
"""

def PrNum(num: int) -> int:
    res = 1
    for i in range(0, num): res *= (i + 1)
    return res

inNumTxt = input('Введите количество элементов набора произведений N = ')
if inNumTxt.isnumeric():
    inNum = int(inNumTxt)
    inList = [i for i in range(1, inNum + 1)]
    outList = list(map(PrNum, inList))
    print(f'Для N = {inNum} набор произведений {outList}')
else: print('Введённая последовательность символов не является натуральным числом.')