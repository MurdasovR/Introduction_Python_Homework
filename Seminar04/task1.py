# Задача 1. Пользователь вводит число, нужно вывести чило pi с заданной точностью(БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)

from math import pi
try:
    number = int(input('Bвeдитe количество знаков точности вычисления числа пи: '))
except ValueError:
    print('Ошибка ввода, попробуйте еще раз')
    quit()
precision = 1 / 10 ** number
flag = 1
p = 0
k = 0
while flag:
    current_add_pi = (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 /(8 * k + 5) - 1 / (8 * k + 6)) / (16 ** k)
    p += current_add_pi
    k += 1
    if current_add_pi < precision: flag = 0
print(f'Число пи рассчитанное  = {p:.{number}f}')
print(f'Число пи из библиотеки = {pi:.{number}f}')