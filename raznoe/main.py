""" 
Практическое задание
1. В консольный файловый менеджер добавить проверку ввода пользователя для всех функции с параметрами (на уроке разбирали на примере одной функции).
2. Добавить возможность изменения текущей рабочей директории.
3. Добавить возможность развлечения в процессе работы с менеджером. Для этого добавить в менеджер запуск одной из игр: “угадай число” или “угадай число (наоборот)”.

"""

# MAIN:
import sys
import os
from core import * # create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from game_adv import game

save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Нужно выбрать одну из команд: list, create_file, create_folder, delete, copy, help или game')
else:
    if command == 'list':
        get_list()

    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)

    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)

    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует названиe')
        else:
            delete_file(name)

    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Отсутствуют названия файла и/или его копии')
        else:
            copy_file(name, new_name)

    elif command == 'change_dir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует названиe')
        else:
            change_dir(name)

    elif command == 'help':
        print('list  -  список файлов и папок')
        print('create_file  -  создание файлов')
        print('create_folder  -  создание папки')
        print('delete  -  удаление файла или папки')
        print('copy  -  копирование файла или папки')

    elif command == 'game':
        game()


save_info('Конец')

