# Здесь выбор режима

from random import randint


def choose_game() -> int:
    print('Выберете с кем Вы будете играть.')
    try:
        typeGame = int(input('Вторым игроком будет 1-человек, 2-бот: '))
        while typeGame not in [1, 2]:
            print('Выбрать нужно из предложенных вариантов.')
            typeGame = int(input('Вторым игроком будет 1-человек, 2-бот: '))
        return typeGame
    except ValueError:
        print('Ведены некорректные данные. Начнём сначала.')  
        choose_game()


def cur_gamer(tg: str) -> int:
    cur_gamer = randint(1, 2)
    if cur_gamer == 1: txt_mas = 'один'
    elif tg == '1': txt_mas = 'два'
    else: txt_mas = 'два (бот)'
    print('\nИгра выберет игрока, чей ход будет первым...')
    print(f'и первым будет играть игрок под номером {txt_mas}\n')
    return cur_gamer


if __name__ == '__main__':
    choose_game()