# Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

def simple_factor1(n):
    sf = []
    i = 2
    while n != 1:
        if n % i !=0:
            i += 1
        else:
            n = n // i
            sf.append(i)
    return sf

def simple_factor2(n):
    sf = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            sf.append(i)
            n = n // i
    if (n != 1): sf.append(n)
    return sf


try:
    number = int(input('Bвeдитe число: '))
except ValueError:
    print('Ошибка ввода, попробуйте еще раз')
    quit()
if (number > 1):
    print(f'Meтoд 1: {number} = {" x ".join(map(str, simple_factor1(number)))}')
    print(f'Meтoд 2: {number} = {" x ".join(map(str, simple_factor2(number)))}')
else:
    print('Число должно быть больше единицы, попробуйте еще раз')