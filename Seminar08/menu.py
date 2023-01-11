def start():
    print('\n' + '━' * 27 + ' СПРАВОЧНИК РАБОТНИКОВ ' + '━' * 27)


def menu_choice(menu_str, offer1, offer2):
    print(f'{offer1}:\n' + '\n'.join(' ' * 18 + str(i + 1) +
          ' - ' + menu_str[i] for i in range(len(menu_str))))
    try:
        choice = int(input(
            f'Введите цифру от 1 до {len(menu_str)} или любой другой символ для {offer2}: '))
        if 0 < choice <= len(menu_str):
            return choice
        else:
            return 0
    except ValueError:
        return 0


def thanks():
    print('━' * 14 + ' СПАСИБО за использование СПРАВОЧНИКА РАБОТНИКОВ ' + '━' * 14 + '\n')
    quit()
