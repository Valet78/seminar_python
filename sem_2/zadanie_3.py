'''
Задание 3. Напишите программу, в которой пользователь будет задавать две строки, 
           а программа - определять количество вхождений одной строки в другой.

Пример :
абвгдабвгд -> 2
абв

'''
def FindStrInStrToOne(str1, str2, indSt):
    return str1.find(str2, indSt)

inStrOne = input('Введите первую строку символов: ')
inStrTwo = input('Введите вторую строку символов: ')
indStart = 0
numIn = 0
lenStr2 = len(inStrTwo)
indFind = FindStrInStrToOne(inStrOne, inStrTwo, indStart)
while indFind != -1:
    numIn += 1
    indStart = indFind + lenStr2
    indFind = FindStrInStrToOne(inStrOne, inStrTwo, indStart)

print (f'Строка {inStrTwo} входит в строку {inStrOne} {numIn} раз')