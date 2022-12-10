'''
Задание 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

Пример: Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

'''
""" 
inNumTxt = input('Введите количество элементов (1+1/n)^n последовательности N = ')
if inNumTxt.isnumeric():
    listRes = []
    inNum = int(inNumTxt)
    sum = 0
    temp = 0
    for i in range(1, inNum + 1):
        temp = (1 + i ** -1) ** i
        listRes.append(temp)
        sum += temp
    

    print(f'\nДля N = {inNum} будет последовательность {listRes}, а сумма этих элементов равна {sum}\n')
else: print('Введённая последовательность символов не является натуральным числом.')

"""

inNumTxt = input('Введите количество элементов (1+1/n)^n последовательности N = ')
if inNumTxt.isnumeric():
    inNum = int(inNumTxt)
    inList = [i for i in range(1, inNum + 1)]
    resPol = lambda x: (1 + x ** -1) ** x
    outList = list(map(resPol, inList))
    summ = sum(outList)
    sumTxt = '{:5f}'.format(summ)
    print(f'\nДля N = {inNum} будет последовательность {outList}, а сумма этих элементов равна {sumTxt}\n')
else: print('Введённая последовательность символов не является натуральным числом.')
