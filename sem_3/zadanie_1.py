""" 
Задание 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число. 

Пример:
['ssss', 'sngujn556', 56] -> Yes 
['56', 'sgnbsb'] -> No
 """

#listMy = ['ssss', 'sngujn556', 56]
#listMy = ['ssss', 'sngujn556', -56]
#listMy = ['ssss', 'sngujn556', 56.35]
listMy = [12.34,'ssss', 'sngujn556']
#listMy = ['56', 'sgnbsb']

res = 'No'
typeTxt = ''
for elem in listMy:
    typeTxt = type(elem)
    if typeTxt == int or typeTxt == float:
        res = 'Yes'
    
print (f'\n{listMy} - > {res}\n') 