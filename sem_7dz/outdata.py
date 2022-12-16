# Модуль взаимодействия с внешними данными
import csv
from os import getcwd
PATHFILE = getcwd() + '\\sem_7dz\\'


def load_data(name_f: str) -> list[str]:                           # Чтение всех данных в список списков
    name_f = PATHFILE + name_f
    try:
        with open(name_f, 'rb') as file_txt:
            list_abon = list(file_txt.read().decode('utf-8').split('\n'))            
            res_list = list([i.split(',') for i in list_abon])
            return res_list
           
    except FileNotFoundError:
        return list([])      


def load_data_csv(name_f: str) -> list[str]:                           # Чтение всех данных в список списков из csv    
    name_f = PATHFILE + name_f
    try:
        with open(name_f) as file_csv:
            res_list = []
            reader = csv.reader(file_csv)
            for i in reader:
                res_list.append(i)

            return res_list
           
    except FileNotFoundError:
        return list([])          


def add_data(name_f: str, txt_data: str = ''):                       # Добавление строки в txt список
    name_f = PATHFILE + name_f
    with open(name_f, "ab") as file_txt:
            file_txt.write(txt_data.encode("utf-8")) 
     

def add_data_csv(name_f: str, txt_data: str = ''):                       # Добавление строки в csv список
    name_f = PATHFILE + name_f
    with open(name_f, 'a', newline='\n') as file_csv:
            # text = txt_data.encode("utf-8")
            text = txt_data
            # print(text)
            wr = csv.writer(file_csv)
            wr.writerow(text)     






if __name__ == '__main__':
    load_data()
    # new_data()