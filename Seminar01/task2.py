# Задача 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('{} \n|{:^5}|{:^5}|{:^5}|{!s:^30}|\n{}'.format('-' * 50, 'X', 'Y', 'Z', '¬(X V Y V Z) = ¬X ⋀ ¬Y ⋀ ¬Z', '-' * 50))
for x in range(2):
    for y in range(2):
        for z in range(2):
            print('|{:^5}|{:^5}|{:^5}|{!s:^30}|'.format(x, y, z, not (x or y or z) == (not x and not y and not z)))
print('-'*50)