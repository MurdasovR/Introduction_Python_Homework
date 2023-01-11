# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def decimal_to_binary(x):
    return str(x) if x < 2 else decimal_to_binary(x // 2) + str(x % 2)

try:
    n = int(input('Bвeдитe число: '))
except ValueError:
    print('Ошибка ввода, попробуйте еще раз')
    quit()
if n < 0 : print('Число не должно быть отрицательным, попробуйте еще раз')
else: print(f'{n} -> {decimal_to_binary(n)}')