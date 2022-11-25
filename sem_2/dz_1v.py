'''
Задание 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:
- 6782 -> 23
- 0,56 -> 11

Вариант решения

'''

def verifNum(verifTxt):
    verRes = True
    listSimv = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    for i in verifTxt:
        if i not in listSimv: verRes = False
    return verRes

def sumNum(inTxt):
    listSimv = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    summ = 0
    for i in inTxt:
        if i in listSimv:
            summ += int(i)
    return summ


inNumTxt = input('Введите число для получения суммы его чисел: ').replace(',', '.')
if verifNum(inNumTxt): 
    print(f'{inNumTxt} - > сумма чисел равна {sumNum(inNumTxt)}')
else: print('Введено некорректное значение. Попробуйте снова.')