def welcome():
    print('\n' + '━' * 27 + ' ТЕЛЕФОННЫЙ СПРАВОЧНИК ' + '━' * 27)


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
    print('━' * 12 + ' Благодарим за использование ТЕЛЕФОННОГО СПРАВОЧНИКА ' + '━' * 12 + '\n')
    quit()


def input_record(new_id, offer):
    new_record = []
    new_record.append(str(new_id))
    for i in range(len(offer)):
        new_record.append(input(f'Введите {offer[i]}: '))
    return [new_record]


def input_id(phonebook, offer):
    flag = 1
    while flag:
        id = input(
            f'Введите число id-записи для {offer} или любые буквы для возврата: ')
        if id.isdigit():
            if index_id(phonebook, int(id)) != -1:
                flag = 0
            else:
                print(f'Записи с id = {id} не существует, попробйте еще раз!')
        else:
            return -1
    return int(id)


def input_change(record, offer, num):
    new_record = [i for i in record]
    match num:
        case 1:
            new_record[1] = (input(f'Введите новую {offer[0]}: '))
        case 2:
            new_record[2] = (input(f'Введите новое {offer[1]}: '))
        case 3:
            new_record[3] = (input(f'Введите новый {offer[2]}: '))
        case 4:
            new_record[4] = (input(f'Введите новое {offer[3]}: '))
    return [new_record]


def index_id(phonebook, id):
    result = -1
    for i in range(len(phonebook)):
        if phonebook[i][0] == str(id):
            result = i
    return result


def new_id(phonebook):
    result = len(phonebook) + 1
    flag = 1
    while flag:
        if index_id(phonebook, result) == -1:
            flag = 0
        else:
            result += 1
    return result