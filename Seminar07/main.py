import menu
import tools
import output
menu_content = [('Просмотр всех записей', 'Поиск записи', 'Добавить запись', 'Изменить запись', 'Удалить запись', 'Экспорт записи'),
                ('Добавить с клавиатуры', 'Импорт из файла import.csv',
                 'Импорт из файла import.vcard'),
                ('Добавить введенный контакт', 'Объединить введенный контакт с существующим')]
input_field = ('фамилию', 'имя', 'телефон', 'описание')
file_export = ('export.csv', 'export.vcard')
phonebook = tools.read_phonebook()
fields = output.fields_count(phonebook)
menu.welcome()
while 1:
    choice = menu.menu_choice(menu_content[0], 'Выберите действие', 'выхода')
    if 0 < choice <= len(menu_content[0]):
        match choice:
            case 1:
                output.print_phonebook_full(phonebook, fields)
            case 2:
                find_str = input('Введите строку для поиска: ')
                find_records = tools.phonebook_find(phonebook, find_str)
                if len(find_records) == 0:
                    print(f"Записи, содержащие '{find_str}' не найдены:")
                else:
                    print(
                        f"Найдено {len(find_records)} записей, содержащих '{find_str}':")
                    output.print_phonebook_part(
                        phonebook, fields, find_records)
            case 3:
                choice = menu.menu_choice(
                    menu_content[1], 'Выберите действие', 'возврата')
                if 0 < choice <= len(menu_content[1]):
                    match choice:
                        case 1:
                            new_record = menu.input_record(
                                menu.new_id(phonebook), input_field)
                        case 2:
                            new_record = tools.read_csv(menu.new_id(phonebook))
                        case 3:
                            new_record = tools.read_vcard(
                                menu.new_id(phonebook))
                    fields = output.fields_correct(fields, new_record)
                    find_records = tools.phonebook_find(
                        phonebook, ''.join([new_record[0][i] for i in [1, 2]]))
                    print('Запись для добавления:')
                    output.print_phonebook_full(new_record, fields)
                    if len(find_records) != 0:
                        print(
                            f'\nВНИМАНИЕ!!! Запись {new_record[0][1]} {new_record[0][2]} уже существует!')
                        output.print_phonebook_part(
                            phonebook, fields, find_records)
                        choice = menu.menu_choice(
                            menu_content[2], 'Выберите действие', 'возврата')
                        if 0 < choice <= len(menu_content[2]):
                            match choice:
                                case 1:
                                    phonebook.append(new_record[0])
                                    print('Новая запись добавлена!\n')
                                case 2:
                                    if len(find_records) > 1:
                                        print(
                                            f'ВНИМАНИЕ!!! Есть {len(find_records)} записей {new_record[0][1]} {new_record[0][2]}!')
                                        choice = menu.menu_choice([f'Объединить с записью id = {phonebook[find_records[i]][0]}' for i in range(
                                            len(find_records))], 'Выберите действие', 'возврата')
                                        if 0 < choice <= len(find_records):
                                            phonebook = tools.union_record(
                                                phonebook, new_record, find_records, choice)
                                            print('Записи объединены!\n')
                                    else:
                                        phonebook = tools.union_record(
                                            phonebook, new_record, find_records)
                                        print('Записи объединены!\n')
                    else:
                        if menu.menu_choice(['Добавить контакт'], 'Выберите действие', 'возврата') == 1:
                            phonebook.append(new_record[0])
                            print('Новая запись добавлена!\n')
            case 4:
                id_change = menu.input_id(phonebook, 'изменения')
                if id_change != -1:
                    print(f'Запись c id = {id_change}')
                    index_change = menu.index_id(phonebook, id_change)
                    output.print_phonebook_part(
                        phonebook, fields, [index_change])
                    choice = menu.menu_choice(
                        [f'Изменить {i}' for i in input_field], 'Выберите действие', 'возврата')
                    if 0 < choice <= len(input_field):
                        new_record = menu.input_change(
                            phonebook[index_change], input_field, choice)
                        print('Предлагаемые изменения:')
                        output.print_phonebook_full(new_record, fields)
                        if menu.menu_choice(['Изменить запись'], 'Выберите действие', 'возврата') == 1:
                            phonebook[index_change][choice] = new_record[0][choice]
                            print(f'Запись c id = {id_change} изменена!\n')
            case 5:
                id_del = menu.input_id(phonebook, 'удаления')
                if id_del != -1:
                    print(f'Запись c id = {id_del} будет удалена')
                    index_del = menu.index_id(phonebook, id_del)
                    output.print_phonebook_part(phonebook, fields, [index_del])
                    if menu.menu_choice(['Удалить запись'], 'Выберите действие', 'возврата') == 1:
                        del phonebook[index_del]
                        print(f'Запись c id = {id_del} удалена!\n')
            case 6:
                id_export = menu.input_id(phonebook, 'экспорта')
                if id_export != -1:
                    print(f'Запись c id = {id_export} будет экспортирована')
                    index_export = menu.index_id(phonebook, id_export)
                    output.print_phonebook_part(
                        phonebook, fields, [index_export])
                    choice = menu.menu_choice(
                        [f'Экспортировать в {i}' for i in file_export], 'Выберите действие', 'возврата')
                    if choice == 1:
                        tools.write_csv(phonebook[index_export])
                        print(
                            f'Запись c id = {index_export} экспортирована в {file_export[choice-1]}!\n')
                    elif choice == 2:
                        tools.write_vcard(phonebook[index_export])
                        print(
                            f'Запись c id = {index_export} экспортирована в {file_export[choice-1]}!\n')
    else:
        tools.write_phonebook(phonebook)
        menu.thanks()