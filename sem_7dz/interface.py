# Модуль взаимодействия с пользователем

from outdata import *


def action_id() -> int:                 # Вывод запроса действий
    try:
        print()
        print('Телефонный справочник.')
        print('Вы можете выполнить следующие действия:')
        print('1. Просмотреть данные справочника.')
        print('2. Найти данные абонента.')
        print('3. Добавить нового абонента.')
        print('4. Импорт данных из файла .txt или .scv')
        print('5. Экспорт данных в файл .txt или .scv')        
        print('________________________')
        print('0. Завершить программу.')
        id_action = int(input('\n Введите необходимое действие: '))
        while id_action not in [1, 2, 3, 4, 5, 0]:
            print('Вы ввели некорректные данные. Будьте внимательны.')
            raise ValueError
        else: return id_action

    except ValueError:
        print('Выбрать можно только указанные действия. Попробуйте снова.')
        action_id()

def show_sprav(in_list: list[str]):         # Вывод на консоль всего списка абонентов
    print()
    print('Фамилия'.ljust(15),'Имя'.ljust(15), 'Отчество'.ljust(15), 'Тел. личный'.ljust(15), 'Тел.рабочий'.ljust(15))
    print('-------------------------------------------------------------------------------')
    for i in in_list:
        if i[0] =='': break
        family, name, otchestvo, lich_nom, work_nom = i
        print(family.ljust(15), name.ljust(15), otchestvo.ljust(15), lich_nom.ljust(15), work_nom.ljust(15)) 
    print()

def add_interface() -> str:                 # Ввод нового абонента
    sogl = False
    res =''
    print('\nВы хотите добавить нового абонента?!')
    try:
        while not sogl: 
            print('Введите данные в формате: "Сидорук Николай Петрович 7(905)8547511 8(956)4561557" (через пробелы).')
            in_list = list(input('Поехали: ').split())
            print('\tПроверяем:')
            print('\tФамилия: '.ljust(15), in_list[0])
            print('\tИмя: '.ljust(15), in_list[1])
            print('\tОтчество: '.ljust(15), in_list[2])
            print('\tТел. личный: '.ljust(15), in_list[3])
            print('\tТел.рабочий: '.ljust(15), in_list[3])  
            sogl_txt = input('Вы согласны (да/нет): ')          
            if sogl_txt == 'да': 
                sogl = True
                res = ",".join(in_list)
            elif sogl_txt == 'нет': 
                sogl = False
                res = ''
            else: raise ValueError
            res += '\n'  
            return res
    
    except ValueError:
        print('Непредвиденная ошибка! Повторим ввод.')
        add_interface()


def seach_abon(in_list: list[str]) -> list[str]:      # Поиск абонента
    res = []
    print('Кого станем искать? Введите через пробел искомые данные (не более 3-х)')
    seach_txt = input('Например, имя и/или фамилию и/или номер в формате *(***)******* абонента): ')
    valid_s, list_s = valid_seach(seach_txt)
    while not valid_s:
        print('\nВы забыли внести данные или неверно их указали. Попробуем снова.')
        print('Кого станем искать? Введите через пробел искомые данные (не более 3-х)')
        seach_txt = input('Например, имя и/или фамилию и/или номер в формате *(***)******* абонента): ')
        valid_s, list_s = valid_seach(seach_txt)
    
    for ii in list_s:  
        for kk in in_list:
            if ii in kk:
                res.append(in_list[in_list.index(kk)])
    # Убираем повторения
    res_new =[]
    for i in res:
        if res_new.count(i) == 0: res_new.append(i)
                   
    return res_new   


def valid_seach(in_txt: str):               # Проверка правильности ввода данных для поиска
    res_bool = True
    if in_txt != '':
        res_list = list(in_txt.split())
        res_list = [i.strip() for i in res_list]    # Убираем лишние пробелы
        if len(res_list) > 3: res_bool = False
        
    else: res_bool = False 
    return res_bool, res_list


def valid_filename() -> str:
    try:
        res_str = input('Введите название файла (.txt или .csv): ').strip()
        if res_str != '':
            res = list(res_str.split('.'))
            if (res[1] == 'txt' or res[1] == 'csv') and res[0] != '':                
                return res_str, res[1]            
        
        raise ValueError

    except ValueError:
        print('Введены некорректные данные. Попробуйте снова.')
        return '', ''




if __name__=='__main__':
    ll = [
            ['Николайчук','Петр','Сергеевич','7(905)4456874','8(042)3456351'], 
            ['Петрук','Игорь','Викторович','7(903)8113435','8(776)8976778'],
            ['Иванов','Сергей','Петрович','7(903)8567465','8(955)4561234'],
            ['Сергеев','Константин','Викторович','7(903)8547565','8(955)4561235'],
            ['Сидорук','Николай','Петрович','7(905)8547511','8(956)4561557']
        ]
    # seach_abon(ll)

   