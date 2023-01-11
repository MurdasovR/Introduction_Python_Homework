# Задача 1218. Петя впервые пришел на урок физкультуры в новой школе. Перед началом урока ученики выстраиваются по росту, в порядке невозрастания. 
#              Напишите программу, которая определит на какое место в шеренге Пете нужно встать, чтобы не нарушить традицию, 
#              если заранее известен рост каждого ученика и эти данные уже расположены по невозрастанию (то есть каждое следующее число не больше предыдущего).
#              Если в классе есть несколько учеников с таким же ростом, как у Пети, то программа должна расположить его после них.
#              Число учеников в классе без Пети принять 25, рост учеников определить случайным образом в интервале от 120 до 190.
#              Рост Пети вводится с клавиатуры

from random import randint
student_growth = [randint(120,190) for x in range(25)]
for i in range(0, len(student_growth)-1):
    for j in range(len(student_growth)-i-1):
        if (student_growth[j]<student_growth[j+1]): 
            student_growth[j], student_growth[j+1] = student_growth[j+1], student_growth[j]
print('Шеренга учеников по росту\nПoзиция:', end=' ')
for i in range(1, len(student_growth)+1):
    print('{:^5}'.format(i), end=' ')
print('\n   Pocт:', end=' ')
for i in range(len(student_growth)):
    print('{:^5}'.format(student_growth[i]), end=' ')
try:
    new_growth = int(input('\nBвeдитe рост нового ученика: '))
except ValueError:
    print('Ошибка ввода, попробуйте еще раз')
    quit()
flag =0
if new_growth > 0:
    for i in range(len(student_growth)):
        if new_growth > student_growth[i]: 
            flag = 1
            break
    i = i + 1 if flag ==1 else i + 2
    print(f'Ученику c ростом {new_growth} нужно встать на позицию {i}')
else:
    print(f'Рост не может быть {new_growth}')