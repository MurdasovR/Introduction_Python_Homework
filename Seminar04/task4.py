# Задача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
try:
    k = int(input('Bвeдитe степень многочлена: '))
except ValueError:
    print('Ошибка ввода, попробуйте еще раз')
    quit()
if k > 0:
    a = [randint(0,100) for _ in range(k+1)]
    str_print = str(a[-2]) + ' * x + ' + str(a[-1])
    if k > 1:
        for i in range(k-1):
            str_print = str(a[i]) + ' * x ** ' + str (i+2) + ' + ' + str_print
    with open('output.txt', 'a') as f:
        f.write(str_print + '\n')
else:
    print('Степень многочлена должна быть больше нуля, попробуйте еще раз')