# Задача 9. В первых двух строках указывается количество детей, любящих манную и овсяную каши (NN и MM).
#           Затем идут NN строк — фамилии детей, которые любят манную кашу, и MM строк с фамилиями детей, любящих овсяную кашу.
#           Гарантируется, что в группе нет однофамильцев.
#           Формат вывода: Количество учеников, которые любят обе каши. Если таких не окажется, в строке вывода нужно написать «Таких нет».
#         Пример 1
#             Ввод
#                 3
#                 2
#                 Васильев
#                 Петров
#                 Васечкин
#                 Иванов
#                 Михайлов
#             Вывод
#                 Таких нет
#         Пример 2
#             Ввод
#                 3
#                 3
#                 Иванов
#                 Петров
#                 Васечкин
#                 Иванов
#                 Петров
#                 Васечкин
#             Вывод
#                 3

n = int(input())
m = int(input())
s1 = {input() for _ in range(n)}
s2 = {input() for _ in range(m)}
num_2 = len(s1.intersection(s2))
if not num_2:
    print('Таких нет')
else:
    print(num_2)
