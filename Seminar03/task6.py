# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на |K| элементов вправо, если K – положительное и влево, если отрицательное. 
# Например: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] сдвиг на  3 -> [7, 8, 9, 0, 1, 2, 3, 4, 5, 6]  
#           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] сдвиг на -3 -> [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]


n = 10
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
try:
    shift = int(input('Bвeдитe число для сдвига: '))
except ValueError:
    print('Ошибка ввода, попробуйте еще раз')
    quit()
print(f'Список:         {a}')
k = shift % n

# Метод 1
print(f'Meтoд 1\ncдвиг на {shift:3d} -> {a[-k:] + a[:-k]}')

# Метод 2
a_shift = [0] * n
for i in range(k):
    a_shift[i] = a [n - k + i]
for i in range(n - k):
    a_shift[i + k] = a [i]
print(f'Meтoд 2\ncдвиг на {shift:3d} -> {a_shift}')

# Метод 3
if k < 0: 
    for i in range(-k):
            a.append(a.pop(0))
else:
    for i in range(k):
        a.insert(0, a.pop())
print(f'Meтoд 3\ncдвиг на {shift:3d} -> {a}')