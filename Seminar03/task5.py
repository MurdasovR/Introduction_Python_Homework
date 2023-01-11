# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.ДОП
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


try:
    k = int(input('Bвeдитe число: '))
except ValueError:
    print('Ошибка ввода, попробуйте еще раз')
    quit()
if k < 0 : print('Число не должно быть отрицательным, попробуйте еще раз')
else: 
    row_fibonacci = [0] * (2 * k + 1)
    if k != 0:
        row_fibonacci[k] = 0
        row_fibonacci[k + 1] = 1
        for i in range(k + 2, 2 * k + 1):
            row_fibonacci[i] = row_fibonacci[i-1] + row_fibonacci[i-2]
        index = 1 if k % 2 else -1
        for i in range(k):
            row_fibonacci[i] = index * row_fibonacci[-i-1]
            index = -index
    print(f'Ряд Негафибоначчи для k = {k} -> {row_fibonacci}')