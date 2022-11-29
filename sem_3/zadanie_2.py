""" 
Задание 2. Напишите программу, которая определит позицию второго вхождения строки 
           в списке либо сообщит, что её нет.
Пример:

список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1

"""

#myList =  ["qwe", "asd", "zxc", "qwe", "ertqwe"]            # ищем: "qwe", ответ: 3
myList =  ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]     # ищем: "йцу", ответ: 5
#myList =  ["йцу", "фыв", "ячс", "цук", "йцукен"]            # ищем: "йцу", ответ: -1
#myList =  ["123", "234", 123, "567"]                        # ищем: "123", ответ: -1
#myList =  []                                                # ищем: "123", ответ: -1

#itemToSearch = "qwe"
itemToSearch = "йцу"
#itemToSearch = "йцу"
#itemToSearch = "123"
#itemToSearch = "123"

def SearchSecondPosition (inSpisok, searTxt) -> int:
    res = 0
    povt = 0     
    for indS in range(len(inSpisok)):
        if inSpisok[indS] == searTxt:
            povt += 1          
            if povt == 2:
                res = indS                
                break                         
                                     
    return res


countIn = myList.count(itemToSearch)
if countIn < 2:
    countIn = -1
    print(f'\nВ списке {myList} ищем "{itemToSearch}" -> -1 (элемент не найден или имеется в единственном экземпляре)\n')
else: 
    countIn = SearchSecondPosition (myList, itemToSearch)
    print(f'\nВ списке {myList} ищем "{itemToSearch}" -> позиция второго "вхождения" - {countIn} \n')
