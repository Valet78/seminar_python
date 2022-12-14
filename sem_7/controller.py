from model import run_game
from logger import log_win
from view import *
from datetime import datetime as dt

def ValueDate(time: dt) -> str:    
    res_day = [str(time.day), str(time.month), str(time.year)]
    res_time = [str(time.hour), str(time.minute), str(time.second)]
    return (".".join(res_day) + ' г. ' + ':'.join(res_time))


def run_prog() -> int:               # Начало игры
    print('\nНачинаем игру.')
    log_win('Начало игры', ValueDate(dt.now()))
    type_game = choose_game()
    text_massage = 'Играют 2 игрока' if type_game == 1 else 'Игра с ботом'
    log_win(text_massage)    
    current_gamer = cur_gamer(str(type_game))
    text_massage = f'Первым ходит игрок номер {current_gamer}'
    log_win(text_massage) 
    win_gamer = run_game(type_game, current_gamer)
    return win_gamer


def end_prog(win_gamer: int):                     # Конец игры и вывод результата принимает номер победителя
    log_win(f'Игра закончена с победой {win_gamer} игрока\n', ValueDate(dt.now()))
    print(f'\nПобедил игрок номер {win_gamer}. Он забирает все конфеты себе.')
    print('\nИ, да, игра окончена!!!\n')


if __name__ == '__main__':
    ValueDate(dt.now())