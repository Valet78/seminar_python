'''
Задание 2. Напишите программу для. проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
¬ - Отрицание 
⋁ - логическое "Или" 
⋀ - логическое "И"

'''

a = [True, False]
for X in a:
    for Y in a:
        for Z in a:
            if not(X or Y or Z) == (not(X) and not(Y) and not(Z)):
                print(f'При значениях [{X}, {Y}, {Z}] \t утверждение истинно.')
            else: print(f'При значениях [{X}, {Y}, {Z}] \t утверждение ложно.')

