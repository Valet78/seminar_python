
from interface import *
from outdata import *

current_tel = load_data('sprav.txt')
if len(current_tel) == 0:
    print('Программа не может найти файл sprav.txt и будет завершена.\n')
    do_it = False
else: do_it = True

while do_it:
    match (action_id()):
        case 1:             # Выводим все данные
            show_sprav(current_tel)

        case 2:             #  Поиск абонента
            one_abon = seach_abon(current_tel)            
            if len(one_abon) != 0:
                show_sprav(one_abon)
            else: print('К сожалению ничего не найдено.')

        case 3:             # Добавляем нового абонента
            text_add = add_interface()
            add_data('sprav.txt', text_add)
            current_tel.clear()            
            current_tel = load_data('sprav.txt')
            
        case 4:             # Импорт данных из файла txt или csv
            file_for_import, rash = valid_filename()
            if file_for_import != '':
                if rash == 'txt':
                    import_tel = load_data(file_for_import)
                    if len(import_tel) != 0:
                        for i in import_tel:
                            if i != ['']:
                                text_add = ','.join(i)
                                add_data('sprav.txt', text_add + '\n')
                        import_tel.clear()
                        current_tel.clear()            
                        current_tel = load_data('sprav.txt')                        
                        
                    else: print(f'Программа не может найти файл {file_for_import}!')   

                if rash == 'csv':
                    import_tel = load_data_csv(file_for_import)
                    if len(import_tel) != 0:    
                        for i in import_tel:
                            if i != ['']:
                                text_add = ','.join(i)
                                add_data('sprav.txt', text_add  + '\n')
                        import_tel.clear()
                        current_tel.clear()            
                        current_tel = load_data('sprav.txt')
                    else: 
                        print(f'Программа не может найти файл {file_for_import}!')              

        case 5:             # Экспорт данных в файл txt или csv
            file_for_export, rash = valid_filename()
            if file_for_export != '':
                if rash == 'txt':
                    for i in current_tel:                        
                        if i != ['']:
                            text_add = ','.join(i)
                            add_data(file_for_export, text_add + '\n')  
            
                if rash == 'csv':
                    for i in current_tel:                        
                        if i != [''] and i != ['\n']:
                            add_data_csv(file_for_export, i)
            
                  
        
        case 0:
            print('\nПрограмма будет закрыта. Удачи Вам!\n')
            do_it = False
