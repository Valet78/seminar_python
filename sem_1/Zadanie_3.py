'''
Задача 3. Напишите программу, которая на вход принимает 5 чисел 
          и находит максимальное из них.
'''

print('Введите 5 чисел для определения максимального  из них.')
for i in range(5):
    inNum = int(input(f'введите {i+1} число: '))
    if i == 0: max = inNum
    if max < inNum: max = inNum
print(f'Максимальное число из введённых равно {max}\n')


'''
a = list(map(int, input().split()))
print(max(a))

'''
