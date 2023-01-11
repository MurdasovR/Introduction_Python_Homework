from random import randint


def bot_turn(a):
    flag = 1
    while flag:
        turn = randint(0, 8)
        if a[turn] == ' ':
            flag = 0
    return turn


def winner(a):
    win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in range(8):
        s = list(set([a[win[i][j]] for j in range(3)]))
        if len(s) == 1 and s[0] != ' ':
            return s[0]
    return 0