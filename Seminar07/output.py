def print_record(record, fields):
    print_line('├', '┼', '┤', '─', fields)
    len_phone = 0
    len_note = 0
    if (len(record[3]) > 14):
        phone = record[3].split(',')
        len_phone = len(phone)
    if (len(record[4]) > 30):
        note = [record[4][(i*30):((i+1)*30)]
                for i in range(len(record[4]) // 30 + 1)]
        len_note = len(note)
    print('│', end='')
    for i in range(len(record)):
        if i == 0:
            print(f' {record[i]:>{fields[i] - 2}} │', end='')
        elif i == 3 and len_phone != 0:
            print(f' {phone[0]:<{fields[i] - 1}}│', end='')
        elif i == 4 and len_note != 0:
            print(f' {note[0]:<{fields[i] - 1}}│', end='')
        else:
            print(f' {record[i]:<{fields[i] - 1}}│', end='')
    print('')
    if len_phone != 0:
        print('│', end='')
        for i in range(1, len_phone):
            print(
                f'{"│".join([" " * fields[i] for i in range(3)])}│ {phone[i]:<{fields[3] - 1}}│', end='')
            print(f' {note[i]:<{fields[4] - 1}}│',
                  end='') if len_note != 0 and i < len_note else print(f'{" " * fields[4]}│', end='')
        print('')
    if len_note != 0 and len_note > len_phone:
        for i in range(1 if len_phone == 0 else len_note - len_phone + 1, len_note):
            print(
                '│' + f'{"│".join([" " * fields[i] for i in range(4)])}│ {note[i]:<{fields[4] - 1}}│')


def print_header(fields_name, fields):
    print_line('┌', '┬', '┐', '─', fields)
    print(
        '│' + "│".join([f'{fields_name[i]:^{fields[i]}}' for i in range(len(fields_name))]) + '│')


def print_line(chr_first, chr_midle, chr_last, chr_fill, fields):
    print(chr_first +
          chr_midle.join([chr_fill * i for i in fields]) + chr_last)


def fields_count(phonebook):
    id_field = max(len(i) for i in list(zip(*phonebook))[0]) + 2
    if id_field < 4:
        id_field = 4
    surname_field = max(len(i) for i in list(zip(*phonebook))[1]) + 2
    if surname_field < 9:
        surname_field = 9
    name_field = max(len(i) for i in list(zip(*phonebook))[2]) + 2
    if name_field < 5:
        name_field = 5
    phone_field = 14
    note_fields = 32
    return [id_field, surname_field, name_field, phone_field, note_fields]


def fields_correct(fields, new_record):
    for i in range(len(new_record)):
        for j in range(len(fields)-2):
            if fields[j] < len(new_record[i][j]) + 2:
                fields[j] = len(new_record[i][j]) + 2
    return fields


def print_phonebook_full(phonebook, fields):
    print_header(('id', 'Фамилия', 'Имя', 'Телефон', 'Описание'), fields)
    for i in phonebook:
        print_record(i, fields)
    print_line('└', '┴', '┘', '─', fields)


def print_phonebook_part(phonebook, fields, part):
    print_header(('id', 'Фамилия', 'Имя', 'Телефон', 'Описание'), fields)
    for i in part:
        print_record(phonebook[i], fields)
    print_line('└', '┴', '┘', '─', fields)