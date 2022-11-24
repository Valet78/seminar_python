'''
Задание 5. Напишите программу, которая принимает на вход координаты двух точек и 
           находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6);  B (2,1)  -> 5,09
- A (7,-5); B (1,-1) -> 7,21

'''
from math import sqrt, floor

print('Введите координаты двух точек для определения расстояния между ними на плоскости')
coordXpointA = int(input('координата X точки А: '))
coordYpointA = int(input('координата Y точки А: '))
coordXpointB = int(input('координата X точки B: '))
coordYpointB = int(input('координата Y точки B: '))
dist = (int(sqrt((coordXpointA - coordXpointB)**2 +(coordYpointA - coordYpointB)**2) * 100) / 100)
distTxt = str(dist).replace('.', ',')
print(f'Расстояние между точками A({coordXpointA}, {coordYpointA}) и B({coordXpointB},{coordYpointB}) -> {distTxt}')