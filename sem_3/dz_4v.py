""" 
Задание 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

    45 -> 101101
    3 -> 11
    2 -> 10

    Вариант решения от преподавателя
 
"""
inNum = 45

def OrdinaryBin(n: int) -> str:
# возвращаяет привычную двоичную запись числа
    return bin(n)[2::]


print(f'{inNum} -> {OrdinaryBin(inNum)}')