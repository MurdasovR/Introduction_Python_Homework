# Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
a = [randint(0,10) for _ in range(20)]
a2 = [0] * len(a)
for i in range(len(a)):
    a2[i] = a [i]

# Метод 1
a_unique = []
[a_unique.append(i) for i in a if i not in a_unique]
print(f'Метод 1 \n{a} -> {a_unique}')

# Метод 2
i = 1
while i < len(a2):
    if a2[i] in a2[:i]:
        a2.pop(i)
    else:
        i += 1
print(f'Метод 2 \n{a} -> {a2}')

# Метод 3
print(f'Метод 3 \n{a} -> {list(dict.fromkeys(a))}')

# Метод 4
print(f'Метод 4 \n{a} -> {list(set(a))}')