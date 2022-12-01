""" 
Задание 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)

Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

 """
# Формируем ряды Фибоначчи 
def Fibonachi(numer):  
    temp = 0 
    for i in range(numer): 
        if i == 0:
            fibonPozList.append(0)
            fibonNegList.append(0)
        elif i == 1 or i == 2:
           fibonPozList.append(1)
           fibonNegList.append(((-1)**(i+1)) * 1)  
        else:
            temp = fibonPozList[i - 1] + fibonPozList[i - 2]      
            fibonPozList.append(temp)
            fibonNegList.append(((-1)**(i+1)) * temp)

# Склеиваем списки для Негафибоначчи
def NegaFibonachi(numer):
    for i in range(numer - 1):
        fibonNegaList.append(fibonNegList[(numer - 1) - i])
    
    for i in range(numer):
        fibonNegaList.append(fibonPozList[i])

inNumTxt = input('\nВведите натуральное число N = ')
if inNumTxt.isnumeric():
    inNum = int(inNumTxt)
    if inNum > 0:
        fibonPozList = []
        fibonNegList = []
        fibonNegaList = []
        
        Fibonachi(inNum + 1)
        NegaFibonachi(inNum + 1)
        
        print(f'\nДля N = {inNum} - > {fibonNegaList}\n')    
    
    else: print('Введено некорректное число.')

else: print('Введено некорректное число.')