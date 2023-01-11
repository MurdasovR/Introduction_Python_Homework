def read_phonebook():
    with open('phonebook.txt', 'r', encoding='utf_8') as file:
        phonebook = [line.rstrip().split(';') for line in file if line != '\n']
    return phonebook


def write_phonebook(phonebook):
    with open('phonebook.txt', 'w', encoding='utf_8') as file:
        file.write('{}\n'.format('\n'.join([";".join(i) for i in phonebook])))
    return


def read_vcard(new_id):
    new_record = []
    new_record.append(str(new_id))
    with open('import.vcard', 'r', encoding='utf_8') as file:
        for line in file:
            if line != '\n':
                string = line.rstrip().split(':')
                if string[0] == 'N':
                    new_record.append(string[1].split(';')[0])
                    new_record.append(string[1].split(';')[1])
                if string[0] == 'TEL':
                    new_record.append(','.join(string[1].split(';')))
                if string[0] == 'NOTE':
                    new_record.append(string[1])
    return [new_record]


def write_vcard(record):
    with open('export.vcard', 'w', encoding='utf_8') as file:
        file.write(
            f'BEGIN:VCARD\nVERSION:3.0\nN:{";".join([record[1], record[2]])}\nTEL:{";".join(record[3].split(","))}\nNOTE:{record[4]}\nEND:VCARD')


def read_csv(new_id):
    with open('import.csv', 'r', encoding='utf_8') as file:
        new_record = file.readline().rstrip().split(';')
    new_record.insert(0, str(new_id))
    return [new_record]


def write_csv(record):
    with open('export.csv', 'w', encoding='utf_8') as file:
        file.write(';'.join(record[1:]))


def phonebook_find(phonebook, str_find):
    result = []
    for i in range(len(phonebook)):
        if str_find in ''.join(phonebook[i]):
            result.append(i)
    return result


def union_record(phonebook, new_record, find_records, num=1):
    for i in range(3, 5):
        if not new_record[0][i] in phonebook[find_records[num-1]][i]:
            phonebook[find_records[num-1]][i] += ',' + new_record[0][i]
    return phonebook