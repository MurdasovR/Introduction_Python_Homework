# Задача 106. На столе случайным образом расположены n монеток. 
#             Некоторые из них лежат вверх решкой, а некоторые – гербом.
#             Положение монетки обоначается целым числом 1, если монетка лежит решкой вверх и 0, если вверх гербом.
#             Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.

from random import randint
try:
    number_coins = int(input('Введите количество монеток: '))
except ValueError:
    print('Ошибка ввода, попробуйте еще раз')
    quit()
if number_coins > 0:
    coin_position = [randint(0,1) for x in range(number_coins)]
    print('Монетки случайно брошены:')
    print(*coin_position)
    coin_position0 = coin_position.count(0)
    coin_position1 = coin_position.count(1)
    print(f'Решкой вверх (1) -> {coin_position1}, Гербом вверх (0) -> {coin_position0}, минимальное из них {min(coin_position0, coin_position1)}')
else:
    print(f'Количество монет не может быть {number_coins}')