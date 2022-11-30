""" 
Задание 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

    45 -> 101101
    3 -> 11
    2 -> 10
 
"""
# рекурсивная фунция
def NumConversion(number, textBin) -> str:
    if number != 0:
        textBin = str(number % 2) + textBin
        number = int(number / 2)
        textBin = NumConversion(number, textBin)
    return textBin


inNumTxt = input('\nВведите натуральное число для преобразование в двоичный код, N = ')
if inNumTxt.isnumeric():
    inNum = int(inNumTxt)
    numInBin = ""
    if inNum == 0: numInBin = "0"
    numInBin = NumConversion(inNum, numInBin)
    print(f'\nЧисло {inNum} в двоичной форме {numInBin}\n')


else: print('Введено некорректное число.')