'''
Задание 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:
- 6782 -> 23
- 0,56 -> 11

'''

inNumTxt = input('Введите число для получения суммы его чисел: ')
inNum = inNumTxt.strip('-')
inNum = inNum.replace(',', '0')
inNum = inNum.replace('.', '0')
sum = 0
if inNum.isnumeric():
    for i in inNum:
        sum += int(i)
    print(f'{inNumTxt} - > сумма чисел равна {sum}')
else: print('Введённая последовательность не является числом. Попробуйте снова.')