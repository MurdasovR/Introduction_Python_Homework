import datetime

def new_id(dictionary):
    k = 1
    flag = 1
    while flag:
        if str(k) not in dictionary.keys():
            flag = 0
        else:
            k += 1
    return str(k)


def input_date(offer):
    flag = True
    while flag:
        try:
            data_string = input(f'{offer} в формате дд.мм.гггг: ')
            if str(type(form_date(data_string))) == "<class 'datetime.date'>":
                flag = False
        except:
            print(f'ОШИБКА!!! Введенные данные {data_string} не являются датой! Попробуйте еще раз! ')
    return data_string


def form_date(string):
    return datetime.date(int(string.split('.')[2]), int(string.split('.')[1]), int(string.split('.')[1]))



def input_record(name_field):
    result = []
    for i in name_field:
        if i == 'Дата рождения':
            result.append(input_date(f'{i}'))
        else:
            result.append(input(f'{i}: '))
    return result


def inpit_id(db, name_field, offer):
    flag = True
    while flag:
        del_key = input(f'Введите {name_field[0]} для {offer} или нажмите Enter для возврата: ')
        if del_key != '':
            if del_key in db.keys():
                flag = False
            else:
                print(f'ОШИБКА! {name_field[0]} = {del_key} не существует. Попробуйте еще раз!')
        else:
            flag = False
    return del_key


def find(db, find_string):
    result = []
    for key, value in db[0].items():
        if (find_string in ' '.join(value[:-2])) or (value[4] in db[4].keys() and find_string in str(db[4][value[4]])) or (value[5] in db[5].keys() and find_string in str(db[5][value[5]])):
            result.append(key)
    for i in range(1, 4):
        for key, value in db[i].items():
            if find_string in str(value):
                result.append(key)
    result = list(dict.fromkeys(result))
    return result


def request_value(db, request_field, request_value, request_type):
    result = []
    if db[0]:
        if request_field == 1:
            for key in db[0].keys():
                if (int(key) < int(request_value) and request_type == 1) or (int(key) == int(request_value) and request_type == 2) or (int(key) > int(request_value) and request_type == 3):
                    result.append(key)
        if request_field == 2:
            for key, value in db[0].items():
                if (request_value > value[0] and request_type == 1) or (request_value == value[0] and request_type == 2) or (request_value < value[0] and request_type == 3):
                    result.append(key)
        if request_field == 3:
            request_date = form_date(request_value)
            for key, value in db[0].items():
                if (request_date > form_date(value[3]) and request_type == 1) or (request_date == form_date(value[3]) and request_type == 2) or (request_date < form_date(value[3]) and request_type == 3):
                    result.append(key)
        if request_field == 4:
            for key, value in db[0].items():
                if (request_value > db[4].get(value[4], [""])[0] and request_type == 1) or (request_value == db[4].get(value[4], [""])[0] and request_type == 2) or (request_value < db[4].get(value[4], [""])[0] and request_type == 3):
                    result.append(key)
        if request_field == 5:
            for key, value in db[0].items():
                if (request_value > db[5].get(value[5], ['', ''])[0] and request_type == 1) or (request_value == db[5].get(value[5], ['', ''])[0] and request_type == 2) or (request_value < db[5].get(value[5], ['', ''])[0] and request_type == 3):
                    result.append(key)
        if request_field == 6:
            for key, value in db[2].items():
                if (request_value > value[0] and request_type == 1) or (request_value == value[0] and request_type == 2) or (request_value < value[0] and request_type == 3):
                    result.append(key)
        if request_field == 7:
            for key, value in db[3].items():
                if (request_value > value[0] and request_type == 1) or (request_value == value[0] and request_type == 2) or (request_value < value[0] and request_type == 3):
                    result.append(key)
        if request_field == 8:
            for key, value in db[1].items():
                if (request_value > value[0][3:] and request_type == 1) or (request_value == value[0][3:] and request_type == 2) or (request_value < value[0][3:] and request_type == 3):
                    result.append(key)
        if request_field == 9:
            for key, value in db[0].items():
                if (int(request_value) > int(db[5].get(value[5], ['0', '0'])[1]) and request_type == 1) or (int(request_value) == int(db[5].get(value[5], ['0', '0'])[1]) and request_type == 2) or (int(request_value) < int(db[5].get(value[5], ['0', '0'])[1]) and request_type == 3):
                    result.append(key)
    return result

            
            
             

    


