# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
#a = [2, 3, 4, 5, 6]
#a = [2, 3, 5, 6]

from random import randint
a = [randint(0,9) for i in range(randint(4,9))]
print(f'{a} -> {list(a[i] * a[- 1 - i] for i in range((len(a) + 1 ) // 2))}')