""" 
Задание 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)

Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

Вариант от преподавателя

 """
# Формируем ряд Фибоначчи 
def Fib(numer: int) -> int:
    if numer in [1, 2]:
        return 1
    elif numer == 0:
        return 0
    else:
        return Fib(numer-1) + Fib(numer-2)

# Формируем ряд Негафибоначчи
def NegaFib(numer: int) -> int:
    return (-1)**(numer+1) * Fib(numer)

# Возвращаем последовательность Фибоначчи
def SeqOfFib(numer: int) -> int:
    listNeg = [NegaFib(i) for i in range(numer+1)][::-1]
    listPoz = [Fib(i) for i in range(1, numer+1)]
    return listNeg + listPoz


inNumTxt = input('\nВведите натуральное число N = ')
if inNumTxt.isnumeric():
    inNum = int(inNumTxt)
    if inNum > 0:
        print(f'\nДля N={inNum} -> {SeqOfFib(inNum)}\n')    
    
    else: print('\nВведено некорректное число.')

else: print('\nВведено некорректное число.')