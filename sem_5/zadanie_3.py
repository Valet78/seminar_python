""" 
3. Задание. Напишите программу, удаляющую из текста все слова, содержащие "абв".
            Пример: 'абвгд гдежз жзе абв ыопыпт' -> ' гдежз жзе ыопыпт'

            Вариант преподавателя!
"""

del_st = lambda x, y: "".join([i for i in x.split() if y not in i])
print(del_st('абвгд гдежз жзе абв ыопыпт', 'абв'))