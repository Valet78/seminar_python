""" 
Задание 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
           между максимальным и минимальным значением дробной части элементов.

Пример:
            [1.1, 1.2, 3.1, 5, 10.01] => 0.19

Вариант решения от преподавателя

"""


myList = [1.1, 1.2, 3.1, 5.003, 10.01]

def SeparateFraction(num: float) -> float:
    # отделяем целую часть от дробной
    listNum = str(num).split('.') 
    return float('0.' + listNum[1])

def MaxVsMinFraction(numList: list[float]) -> float:
    # создаём список из дробных частей
    newList = [SeparateFraction(i) for i in numList if int(i) != float(i)]
    print(newList)
    # возвращаем разницу между макс и мин
    return max(newList) - min(newList)

print(f'\nРазница между максимальным и минимальным значением дробной части элементов списка \n {myList} равна {MaxVsMinFraction(myList)}\n')
