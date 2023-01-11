# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#a = [1.1, 1.2, 3.1, 5, 10.01]

from random import randint, uniform
a = []
for i in range(randint(4,15)):
    if not range(randint(0,5)):
        a.append(randint(0,15))
    else:
        a.append(round(uniform(0,15), 2))
flag = 1
for i in a:
    if type(i) == float:
        fractional_part = i - int(i)
        if flag:
            a_min = a_max = fractional_part
            flag = 0
        else:
            if fractional_part > a_max: a_max = fractional_part
            if fractional_part < a_min: a_min = fractional_part 
print('Вариант 1: {} => {:.2f}'.format(a, a_max - a_min))
print('Вариант 2: {} => {:.2f}'.format(a, max([i - int(i) for i in a if type(i) == float]) - min([i - int(i) for i in a if type(i) == float])))