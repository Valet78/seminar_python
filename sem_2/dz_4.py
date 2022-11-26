'''
Задание 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
           Найдите произведение элементов на указанных позициях. Позиции хранятся в 
           файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант 
           минимум - ввести позиции в консоли)  
           
    Пример: -2 -1 0 1 2           
            Позиции: 0,1 -> 2

'''

from os import getcwd

inNumTxt = input('\nВведите количество элементов списка N = ')
if inNumTxt.isnumeric():
    listRes = []    
    inNum = int (inNumTxt)
    pathFile = getcwd() + '\\sem_2\\file.txt'
    proizv = 1
    
    for i in range(-inNum, inNum + 1):
        listRes.append(i)
      
    try:
        with open(pathFile, "r") as fileTxt:
            listPoz = fileTxt.readlines()
            listPoz = [line.rstrip() for line in listPoz]    # Убираем сиволы переноса строки \n   
        for i in listPoz:
            proizv *= listRes[int(i)]
        
        print(f'\nПроизведение элементов списка -{inNum}...{inNum} на позициях {listPoz} - > {proizv}\n')

    except:
        print('\nНе удалось открыть файл "file.txt"\n')

    # print(f'\nДля N = {inNum} будет последовательность {listRes}, а сумма этих элементов равна {sum}\n')
else: print('Введённая последовательность символов не является натуральным числом.')
