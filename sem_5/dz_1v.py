""" 
Задание 1. Создайте программу для игры с конфетами человек против человека.

*' Условие задачи: 
        На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. 
        Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
        Все конфеты оппонента достаются сделавшему последний ход.

a) Добавьте игру против бота

"""

from random import randint

oneCandy, twoCandy = 0, 0   # количество конфет у игроков
numCandy = 117

print('\nНачинаем игру.')
try:
    typeGame = int(input('Вторым игроком будет 1-человек, 2-бот: '))
    while typeGame not in [1, 2]:
        print('Выбрать нужно из предложенных вариантов.')
        typeGame = int(input('Вторым игроком будет 1-человек, 2-бот: '))

    currentGamer = randint(1, 2)
    print(f'\nПервым будет играть {currentGamer} игрок')

    while numCandy != 0:
        if typeGame == 2:
            if currentGamer == 2: 
                resBot = lambda x: x if x <= 28 else randint(1, 28)
                minusCandy = resBot(numCandy)
                print(f'Второй игрок забрал {minusCandy} из {numCandy}')
            else: minusCandy = int(input(f'Игрок {currentGamer}, сколько конфет Вы зеберёте из {numCandy}? - '))
        else: minusCandy = int(input(f'Игрок {currentGamer}, сколько конфет Вы зеберёте из {numCandy}? - '))
        
        StepGame = lambda x, y: True if y <= 28 and y <= x else False
        NumGame = lambda x: 1 if x == 2 else 2
        if StepGame(numCandy, minusCandy): 
            numCandy -= minusCandy
            if currentGamer == 1: oneCandy += minusCandy
            else: twoCandy += minusCandy 
            currentGamer = NumGame(currentGamer)
        else: print('Вы можете одновременно забрать 28 конфет и не более оставшихся.')
    print(f'\nПобедил игрок номер {NumGame(currentGamer)}\n')

except ValueError:
     print('Ведены некорректные данные. Начнём сначала.')  