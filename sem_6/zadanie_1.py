""" 
Задание 1. Вводятся названия городов в одну строчку через пробел. Необходимо определить функцию map,
            которая бы возвращала названия городов только длиной более 5 символов. Вместо остальных названий -
            строку с дефисом ("-").
            Сформировать список из полученных значений и отобразить его на экране в одну строчку через пробел.

Ввод:
        Москва Уфа Вологда Тула Владивосток Хабаровск
Вывод:
        Москва - Вологда - Владивосток Хабаровск

"""

def OutStr(strIn: str) -> list[str]:
    if len(strIn) < 5: return '-'
    return strIn

print()
inStr = input('Введите через пробел названия городов: ').split()
for i in list(map(OutStr, inStr)): print(i, end=' ')
print('\n')