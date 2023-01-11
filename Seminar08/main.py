import json
import menu
import output
import tools
db = [{}, {}, {}, {}, {}, {}]
db_file_name = ('worker', 'addrs', 'email', 'tel', 'dept', 'post')
db_name = ('Работники', 'Адреса', 'E-mail', 'Телефоны', 'Отделы', 'Должности')
tab_name = (('id работника', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'id отдела', 'id должности'),
            ('id работника', 'Город', 'Улица', 'Дом', 'Квартира'),
            ('id работника', 'E-mail'), ('id работника', 'Телефон'),
            ('id отдела', 'Название отдела'), ('id должности', 'Название должности', 'Оклад'),
            ('id работника', 'ФИО', 'Дата рождения', 'Отдел', 'Должность', 'E-mail', 'Телефон', 'Адрес', 'Оклад'))
tab_fields = (('^9', '<23', '<23', '<23', '^10', '^9', '^9'), ('^9', '<28', '<28', '<15', '<15'), ('^9', '<22'),  ('^9', '<12'), ('^9', '<15'), ('^9', '<20', '>11'),
              ('^9', '<23', '^10', '<15', '<20', '<22', '<12', '<28', '>11'))
offer = (('Просмотр всех работников', 'Отчеты по Базам данных', 'Поиск по Базам данных', 'Добавление нового работника', 'Удаление работника', 'Работа с Базами данных'),
         ('Просмотр базы', 'Добавить запись', 'Изменить запись', 'Удалить запись'))
for i in range(len(db_file_name)):
    try:
        with open(f'{db_file_name[i]}.json', 'r', encoding='utf_8') as file:
            db[i] = json.load(file)
    except:
        pass
menu.start()
flag1 = True
while flag1:
    main_choice = menu.menu_choice(offer[0], 'Выберите действие', 'выхода')
    match main_choice:
        case 1:
            output.print_pivot_table(db, tab_name[6], tab_fields[6], db[0].keys())
        case 2:
            request_field = menu.menu_choice(tab_name[6], 'Выберите поле для формирования отчета', 'возврата')
            if request_field != 0:
                if request_field == 3:
                    request_value = tools.input_date('Введите дату для формирование отчета')
                else:
                    request_value = input('Введите значение для формирование отчета или нажмите Enter для возврата: ')
                if request_value != '':
                    flag2 = True
                    while flag2:
                        request_type = menu.menu_choice([f'Значения в поле "{tab_name[6][request_field-1]}" меньше "{request_value}"', f'Значения в поле "{tab_name[6][request_field-1]}" равны "{request_value}"', f'Значения в поле "{tab_name[6][request_field-1]}" больше "{request_value}"'], 'Выберите тип отчета', 'возврата')
                        if request_type != 0:
                            find_request = tools.request_value(db, request_field, request_value, request_type)
                            if len(find_request) == 0:
                                print(f"ДАННЫЕ НЕ НАЙДЕНЫ!!!")
                            else:
                                output.print_pivot_table(db, tab_name[6], tab_fields[6], find_request)
                        else:
                            flag2 = False
        case 3:
            find_str = input('Введите строку для поиска с учетом регистра или нажмите Enter для возврата: ')
            if find_str != '':
                find_records = tools.find(db, find_str)
                if len(find_records) == 0:
                    print(f"Сведения о работнике, содержащие '{find_str}' не найдены!")
                else:
                    output.print_pivot_table(db, tab_name[6], tab_fields[6], find_records)
        case 4:
            print('Добавление нового работника:')
            new_key = tools.new_id(db[0])
            for i in range(4):
                db[i][new_key] = tools.input_record(tab_name[i][1:])
            for i in range(4, 6):
                if db[0][new_key][i] != '' and (db[0][new_key][i] not in db[i].keys()):
                    db[i][db[0][new_key][i]] = tools.input_record(tab_name[i][1:])
            print('Добавлен новый работник:')
            output.print_pivot_table(db, tab_name[6], tab_fields[6], [new_key])
        case 5:
            del_key = tools.inpit_id(db[0], tab_name[0], 'удаления')
            if del_key != '':
                print('ВНИМАНИЕ! Работник будет удален:')
                output.print_pivot_table(db, tab_name[6], tab_fields[6], [del_key])
                if menu.menu_choice(['Удалить'], 'Выберите действие', 'возврата') == 1:
                    for i in range(4):
                        db[i].pop(del_key, '')
                    print(f'Работник с id = {del_key} удален!')
        case 6:
            baze_choice = menu.menu_choice(db_name, 'Выберите базу данных', 'возврата')
            if baze_choice != 0:
                flag3 = True
                while flag3:
                    print(f'База "{db_name[baze_choice - 1]}", ', end = '')
                    k3 = menu.menu_choice(offer[1], 'выберите действие', 'возврата')
                    if k3 != 0:
                        match k3:
                            case 1:
                                output.print_table(db[baze_choice-1], tab_name[baze_choice-1], tab_fields[baze_choice-1], db_name[baze_choice - 1], db[baze_choice-1].keys())
                            case 2:
                                if baze_choice in [1, 2, 3, 4]:
                                    print('ПРЕДУПРЕЖДЕНИЕ! "id работника" является общим ключем для баз "' + '", "'.join(db_name[:-2]) + '"!')
                                    print(f'Поэтому добавление новой записи в базу "{db_name[baze_choice - 1]}" добавит пустые записи с таким же "id работника" в базы "' + '", "'.join([i for i in db_name[:-2] if i != db_name[baze_choice - 1]]) + '"!')
                                    print('Рекомендовано пользоваться разделом главного меню "Добавление нового работника"!')
                                if menu.menu_choice(['Продолжить добавление'], 'Выберите действие', 'возврата') == 1:
                                    new_key = tools.new_id(db[baze_choice-1])
                                    db[baze_choice-1][new_key] = tools.input_record(tab_name[baze_choice-1][1:])
                                    print(f'В базу "{db_name[baze_choice - 1]}" добавлена новая запись:')
                                    output.print_table(db[baze_choice - 1], tab_name[baze_choice - 1], tab_fields[baze_choice - 1], db_name[baze_choice - 1], [new_key])
                                    if baze_choice in [1, 2, 3, 4]:
                                        for i in [1, 2, 3, 4]:
                                            if i != baze_choice:
                                                db[i-1][new_key] = ['' for _ in range(len(tab_name[i-1])-1)]
                                        print(f'Добавлены пустые записи с таким же "id работника" в базы "' + '", "'.join([i for i in db_name[:-2] if i != db_name[baze_choice - 1]]) + '"!')
                            case 3:
                                edit_key = tools.inpit_id(db[baze_choice - 1], tab_name[baze_choice - 1], 'изменения')
                                if edit_key != '':
                                    print(f'Запись базы "{db_name[baze_choice - 1]}" для изменения:')
                                    output.print_table(db[baze_choice - 1], tab_name[baze_choice - 1], tab_fields[baze_choice - 1], db_name[baze_choice - 1], [edit_key])
                                    edit_field = menu.menu_choice(tab_name[baze_choice-1][1:], 'Выберите поле', 'изменения')
                                    if edit_field != 0:
                                        db[baze_choice-1][edit_key][edit_field - 1] = input(f'Введите новое значение поля "{tab_name[baze_choice-1][edit_field]}": ')
                                        print(f'Запись с {tab_name[baze_choice - 1][0]} = {edit_key} в базе "{db_name[baze_choice - 1]}" изменена:')
                                        output.print_table(db[baze_choice - 1], tab_name[baze_choice-1], tab_fields[baze_choice-1], db_name[baze_choice - 1], [edit_key])
                            case 4:
                                del_key = tools.inpit_id(db[baze_choice - 1], tab_name[baze_choice - 1], 'удаления')
                                if del_key != '':
                                    print(f'Запись базы "{db_name[baze_choice - 1]}" для удаления:')
                                    output.print_table(db[baze_choice - 1], tab_name[baze_choice - 1], tab_fields[baze_choice - 1], db_name[baze_choice - 1], [del_key])
                                    if baze_choice in [1, 2, 3, 4]:
                                        print('ПРЕДУПРЕЖДЕНИЕ! "id работника" является общим ключем для баз "' + '", "'.join(db_name[:-2]) + '"!')
                                        print(f'Поэтому при удалении записи из базы "{db_name[baze_choice - 1]}" будут удалены записи с таким же "id работника" из баз "' + '", "'.join([i for i in db_name[:-2] if i != db_name[baze_choice - 1]]) + '"!')
                                    if menu.menu_choice(['Удалить'], 'Выберите действие', 'возврата') == 1:
                                        if baze_choice in [1, 2, 3, 4]:
                                            for i in range(4):
                                                db[i].pop(del_key, '')
                                            print(f'Записи с "id работника" = {del_key} удалены из баз "' + '", "'.join(db_name[:-2]) + '"!')
                                        else:
                                            db[baze_choice-1].pop(del_key, '')
                                            print(f'Запись с "{tab_name[baze_choice - 1][0]}" удалена из базы "{db_name[baze_choice - 1]}"!')
                            case 0:
                                flag3 = False
                    else:
                        flag3 = False





        
                        
                



            






        case 0:
            flag1 = False








for i in range(len(db_file_name)):
     with open(f'{db_file_name[i]}.json', 'w', encoding='utf_8') as file:
        json.dump(db[i], file, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
menu.thanks()