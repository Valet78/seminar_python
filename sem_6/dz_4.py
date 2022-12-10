'''
Задание 5. Реализуйте алгоритм перемешивания списка.

'''
from random import randint 
num = 20        # количество элементов в списке


""" 
listDoom = []
listMix = []



def listMixOut(listIn):
    indList = []
    index = 0
    
    while len(indList) != num:
        index = randint(0, num - 1)  # создаём список индексов случайным способом
        if index not in indList:
            indList.append(index)
    for id in indList:
        listMix.append(listDoom[id])

for it in range(num):                       # Заполняем исходный список
    listDoom.append(randint(1, 99))
print (f'\nИсходный список: \t {listDoom}')
listMixOut(listDoom)
print(f'Перемешанный список: \t {listMix}\n')

 """

def RandList(numIn: int) -> list[int]:
    indList = []
    while len(indList) != numIn:
        index = randint(0, numIn - 1)  # создаём список индексов случайным способом
        if index not in indList:
            indList.append(index)
    return indList

listDoom = [randint(1, 99) for i in range(num)]           # Заполняем исходный список
print (f'\nИсходный список: \t {listDoom}')
listZero = RandList(num) 
mix = lambda x: listDoom[x]
listMix = list(map(mix, listZero))

print(f'Перемешанный список: \t {listMix}\n')

