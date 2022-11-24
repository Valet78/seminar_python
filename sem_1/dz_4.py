'''
Задание 4. Напишите программу, которая по заданному номеру четверти, 
           показывает диапазон возможных координат точек в этой четверти (x и y).

'''
print('Введите номер координатной четверти (от 1 до 4)')
inNum = int(input('N = '))
rangeNum = [1, 2, 3, 4]
rangeX = ''
rangeY = ''
if inNum in rangeNum:
    match inNum:
        case 1: 
            rangeX = '(0, +ထ )'
            rangeY = '(0, +ထ )'
        case 2: 
            rangeX = '(0, -ထ )'
            rangeY = '(0, +ထ )'
        case 3: 
            rangeX = '(0, -ထ )'
            rangeY = '(0, -ထ )'
        case 4: 
            rangeX = '(0, +ထ )'
            rangeY = '(0, -ထ )'
    print(f'Для {inNum} координатной четверти X находится в диапазоне {rangeX}, а Y - {rangeY}')
else: print('Введены некорректные значения. Попробуйте снова.')
