# Задача 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


input_string = input('Введите номер координатной четверти: ')
if input_string.isdigit():
    quarter_number = int(input_string)
    match quarter_number:
        case 1: print('1-я четверть: x > 0 и y > 0')
        case 2: print('2-я четверть: x < 0 и y > 0')
        case 3: print('3-я четверть: x < 0 и y < 0')
        case 4: print('4-я четверть: x > 0 и y < 0')
        case _: print(f'Четверти c номером {quarter_number} не существует')
else: print(f'Ошибка! "{input_string}" не является цифрой! Попробуйте еще раз. ')