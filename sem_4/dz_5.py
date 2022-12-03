""" 
Задание 5. Даны два файла, в каждом из которых находится запись многочлена. 
           Задача - сформировать файл, содержащий сумму многочленов.
    
    В file1.txt: 2*x**2 + 4*x + 5
    В file2.txt: 4*x**2 + 1*x + 4
    
    Результирующий файл: 6*x**2 + 5*x + 9

"""

import sympy
from os import getcwd
PATHFILE = getcwd() + '\\sem_4\\'

def FileOperation(nameFile: str, regim: str, strSave = ''):
    pFile = PATHFILE + nameFile
    try:
        with open(pFile, regim) as fileTxt:
            if regim == 'r': 
                return fileTxt.read().split('\n')[0]            # Читаем и убираем сиволы переноса строки \n 
            elif regim in ['w', 'a'] : fileTxt.write(strSave + '\n') 

    except FileNotFoundError:
        print('Файл не найден или невозможно его открыть!')



dataTxt = FileOperation('file1_5.txt', 'r') + " + " + FileOperation('file2_5.txt', 'r')
dataForSave = str(sympy.powsimp(dataTxt))
FileOperation('file_5.txt', 'a', dataForSave) # Запись результатат в файл