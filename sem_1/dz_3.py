'''
Задание 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
           выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34;  y=-30 -> 4
- x=2;   y=4   -> 1
- x=-34; y=-30 -> 3

'''

print('Введите координаты точки (X и Y), где X ≠ 0 и Y ≠ 0 ')
inX = int(input('X = '))
inY = int(input('Y = '))
quarter = ''

if inX > 0 and inY > 0: quarter = 'в 1 четверти'
elif inX < 0 and inY > 0: quarter = 'во 2 четверти'
elif inX < 0 and inY < 0: quarter = 'в 3 четверти'
elif inX > 0 and inY < 0: quarter = 'в 4 четверти'
elif inX == 0 and inY != 0: quarter = 'на оси 0Y'
elif inX != 0 and inY == 0: quarter = 'на оси 0X'
else: quarter = 'в центре системы координат'
print(f'Точка с координатами ({inX}, {inY}) находится {quarter}')
