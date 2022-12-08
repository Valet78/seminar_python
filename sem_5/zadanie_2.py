""" 
Задание 2. Дан список чисел. Создайте список, в который попадают числа, описываемые 
           возрастающую последовательность. Порядок элементов менять нельзя.

Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

"""

from random import randint


def SelList(rr: list[int]) -> list[int]:
    mem = [rr[0]]
    for i in range(1, len(rr)):
        if rr[i] > rr[i-1]: mem.append(rr[i])           
    return mem



def RenderList(inList: list[int]) -> list[int]:
    num, step, ind, k = len(inList), 1, 0, 0       
    LList = []
    while ind != num:       # 0 .. 7
        while step < num - ind: 
            tempList = [inList[i] for i in range(ind, num, step)]
            if len(tempList) > 1:
                tempList = SelList(tempList)               
                if len(tempList) > 1 and not LList.count(tempList): LList.append(tempList)                       
            step +=1          
        step = 1
        ind += 1     
        
    return LList


# Оснавная часть
inList = [1, 5, 2, 3, 4, 6, 1, 7]     # Заданная последовательность
print(f'\nДан список чисел: \t\t\t\t\t{inList}')
outList = RenderList(inList)
# Вывод всех возможных вариантов последовательностей
# print('Для которого возможны варианты возврастающих последовательностей:')
# for i in outList: print(i)

# Вывод случайной последовательности из списка возможных
#lenL = len(outList) - 1
ind = randint(0, len(outList) - 1)
print(f'Одна из возможных возрастающих последовательностей: \t{outList[ind]}\n')