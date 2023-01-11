# Задача 1126. Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

try:
    number = int(input('Введите число: '))
except ValueError:
    print('Ошибка ввода, попробуйте еще раз')
    quit()
divider = 2
while number % divider !=0: divider+=1
print(f'Наименьший натуральный делитель числа {number}, отличный от 1, равен: {divider}')