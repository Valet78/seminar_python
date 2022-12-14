# Запись результата
from os import getcwd

def log_win(strMassage: str, strTime: str = '\t'):
    pathFile = getcwd() + '\\sem_7\\log.txt'
    with open(pathFile, 'a', encoding='utf-8') as fileTxt:
        fileTxt.write(f'{strTime}\t{strMassage}\n')      


if __name__ == '__main__':
    log_win('Проверка', '14.12.2022 г. 00:10:00')
    # log_win('Test 2')