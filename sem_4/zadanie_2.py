""" 
Задание 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

1) с помощью математических формул нахождения корней квадратного уравнения (D = b^2-4ac, x1 = (-b+/- sqtr(D))/2*a)

2) с помощью дополнительных библиотек Python(sympy, scipy)(Дополнительно)


"""
import sympy as sy

def SposobOne(inA, inB, inC):
    diskr = inB**2 - 4 * inA * inC    
    if diskr < 0: print(f'\tВ уранении {inA}x² + {inB}x + {inC} = 0 нет действительных корней.\n')
    elif diskr == 0: 
        temp = round(-inB / (2 * inA), 3)
        print(f'\tУранение {inA}x² + {inB}x + {inC} = 0 имеет единственный корень x = {temp}.\n')
    else:
        x1 = round((-inB - diskr**0.5) / (inA * 2), 3)
        x2 = round((-inB + diskr**0.5) / (inA * 2), 3)
        print(f'\tУранение {inA}x² + {inB}x + {inC} = 0 имеет два корня x1 = {x1}, x2 = {x2}.\n')

def SposobTwo(inA, inB, inC):    
    x = sy.Symbol('x')
    res = sy.solve(inA*(x**2) + inB*x + inC, x)
    print(f'\tУранение {inA}x² + {inB}x + {inC} = 0 имеет следующие корни {res}\n')



inNum = list(map(int, input('Введите через пробел значения A, B и C квадратного уравнения Ax² + Bx + C = 0 (A≠0): ').split()))
A, B, C = inNum
print('\nВариант 1:')
SposobOne(A, B, C)
print('\nВариант 2:')
SposobTwo(A, B, C)