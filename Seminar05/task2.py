# Задача 2. Создайте программу для игры в ""Крестики-нолики"".

def print_place(a):
    print('     1   2   3')
    print('   ┏━━━┳━━━┳━━━┓')
    for i in range(3):
        print(f' {i+1} ┃', end='')
        for j in range(3):
            if a[i][j] == -1:
                s = 'X'
            elif a[i][j] == 1:
                s = 'O'
            else:
                s = ' '
            print(f' {s} ┃', end='')
        if i < 2:
            print('\n   ┣━━━╋━━━╋━━━┫')
        else:
            print('\n   ┗━━━┻━━━┻━━━┛')


def busy_place(a, i, j):
    return False if not a[i][j] else True


def winner(a):
    for i in range(3):
        s = list(set(a[i]))
        if len(s) == 1 and s[0] != 0:
            return s[0]
        s = list(set(list(zip(*a))[i]))
        if len(s) == 1 and s[0] != 0:
            return s[0]
    s = list(set([a[i][i] for i in range(3)]))
    if len(s) == 1 and s[0] != 0:
        return s[0]
    s = list(set([a[2-i][i] for i in range(3)]))
    if len(s) == 1 and s[0] != 0:
        return s[0]
    return 0


a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
name = ['крестик', 'нолик']
victory = 0
player = 0
print_place(a)
while not victory:
    input_correct = 0
    print(f'Ход {player+1}-го игрока, играющего {name[player]}ами.')
    while not input_correct:
        try:
            i, j = map(int, input(
                f'Чтобы поставить в клетку {name[player]}, введите через пробел номер строки и столбца: ').split())
            if 0 < i < 4 and 0 < j < 4:
                if not busy_place(a, i-1, j-1):
                    input_correct = 1
                else:
                    print(
                        f'Клетка в строке {i} и столбце {j} уже занята, попробуйте еще раз!')
            else:
                print(
                    f'Клетки в строке {i} и столбце {j} не существует, попробуйте еще раз!')
        except ValueError:
            print('Нужно ввести две цифры через пробел, попробуйте еще раз')

    a[i-1][j-1] = -1 if player == 0 else 1
    print_place(a)
    if not winner(a):
        player = 1 if not player else 0
    else:
        victory = 1
print(f'Победил игрок {player+1}, игравший {name[player]}ами!!!')