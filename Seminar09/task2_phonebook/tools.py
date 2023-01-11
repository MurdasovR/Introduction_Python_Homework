import json

def write_vcard(record):
    with open('export.vcard', 'w', encoding='utf_8') as file:
        try:
            file.write(f'BEGIN:VCARD\nVERSION:3.0\nN:{";".join([record[0], record[1]])}\nTEL:{";".join(record[2].split(","))}\nNOTE:{", ".join(record[2].split(","))}\nEND:VCARD')
            return True
        except:
            return False


def phonebook_find(phonebook, str_find):
    result = []
    for key in phonebook:
        if str_find in ''.join(phonebook[key]):
            result.append(key)
    return result


def read_phonebook():
    try:
        with open('phonebook.json', 'r', encoding='utf_8') as file:
            phonebook = json.load(file)
            return phonebook
    except:
        return {}


def write_phonebook(phonebook):
    with open('phonebook.json', 'w', encoding='utf_8') as file:
        json.dump(phonebook, file, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))


def init_dict(phonebook, dictionary):
    for key, value in phonebook.items():
        dictionary[key] = value


def new_id(dictionary):
    k = 1
    flag = 1
    while flag:
        if str(k) not in dictionary.keys():
            flag = 0
        else:
            k += 1
    return str(k)


def str_phonebook(book, keys):
    s = ''
    if book:
        for key in keys:
            s += f'id: {key}\nИмя: {book[key][0]} {book[key][1]}\nТел: {", ".join(book[key][2].split(","))}\nОписание: {", ".join(book[key][3].split(","))}\n\n'
    else:
        s = 'телефонный справочник пока пуст'
    return s
