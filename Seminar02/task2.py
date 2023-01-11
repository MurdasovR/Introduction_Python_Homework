# Задача 2. Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

def summa1N(N):
    return 1 if N==1 else N+summa1N(N-1)

try:
    number = int(input('Введите число: '))
except ValueError:
    print('Ошибка ввода, попробуйте еще раз')
    quit()
if number < 1: print('Для вычисления суммы число не должно быть меньше 1')
else: 
    print(f'Способ 1: сумма чисел между 1 и {number} включительно равна {summa1N(number)}')
    print('Способ 2: сумма чисел между 1 и {} включительно равна {}'.format(number, sum(i for i in range(1, number+1))))
