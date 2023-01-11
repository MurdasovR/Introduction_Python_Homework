# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# 		Пример:
# 		6 -> да
# 		7 -> да
# 		1 -> нет

input_string = input('Введите цифру дня недели: ')
if input_string.isdigit():
    number_day_of_week = int(input_string)
    if 0 < number_day_of_week < 6: 
        print(f'{number_day_of_week} -> нет')
    elif 5 < number_day_of_week < 8:
        print(f'{number_day_of_week} -> да')
    else:
        print(f'дня недели c цифрой {number_day_of_week} не существует')
else:
    print(f'Ошибка! "{input_string}" не является цифрой! Попробуйте еще раз. ')