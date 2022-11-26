'''
Задание 5. Реализуйте алгоритм перемешивания списка.

'''
import random
listDoom = []
listMix = []
num = 20        # количество элементов в списке


def listMixOut(listIn):
    indList = []
    index = 0
    
    while len(indList) != num:
        index = random.randint(0, num - 1)  # создаём список индексов случайным способом
        if index not in indList:
            indList.append(index)
    for id in indList:
        listMix.append(listDoom[id])


for it in range(num):                       # Заполняем исходный список
    listDoom.append(random.randint(1, 99))
print (f'\nИсходный список: \t {listDoom}')
listMixOut(listDoom)
print(f'Перемешанный список: \t {listMix}\n')

