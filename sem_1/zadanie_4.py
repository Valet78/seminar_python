'''
Задача 4. Напишите программу, которая будет на вход принимать 
          число N и выводить числа от -N до N

'''

inNum = int(input('Ввведите число N для вывода чисел из диапазона -N...N: '))

strRes = ''
for i in range(-inNum, inNum + 1):
    strRes += str(i)
    if i != inNum: strRes += ', '

print(f'Числа из диапазона -{inNum}...{inNum} -> [{strRes}]')   
    
    
'''
a = list(map(int, input().split()))
print(max(a))

'''