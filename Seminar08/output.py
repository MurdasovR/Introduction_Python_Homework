def print_line(chr_first, chr_midle, chr_last, chr_fill, fields):
    print(chr_first +
          chr_midle.join([chr_fill * (int(i[1:]) + 2) for i in fields]) + chr_last)


def print_header(fields_name, fields):
    print_line('┌', '┬', '┐', '─', fields)
    for i in range(2):
        print('│', end='')
        for j in range(len(fields)):
            if len(fields_name[j]) <= int(fields[j][1:]):
                if i == 0:
                    print(f' {str(fields_name[j]):^{int(fields[j][1:])}} │', end='')
                else:
                    print(f' {" ":^{int(fields[j][1:])}} │', end='')
            else:
                print(f' {str(fields_name[j].split()[i]):^{int(fields[j][1:])}} │', end='')
        print()


def print_pivot_table(db, fields_name, fields, size):
    print_header(fields_name, fields)
    if db[0]:
        for key in size:
            print_line('├', '┼', '┤', '─', fields)
            for i in range(3):
                if i == 0:
                    print(f'│ {key:{fields[0]}} │ {db[0][key][i]:{fields[1]}} │ {db[0][key][3]:{fields[2]}} │ {db[4].get(db[0][key][4], [""])[0]:{fields[3]}} │ {db[5].get(db[0][key][5], ["", ""])[0]:{fields[4]}} │ {db[2][key][0]:{fields[5]}} │ {db[3][key][0]:{fields[6]}} │ {db[1][key][0] + ",":{fields[7]}} │ {db[5].get(db[0][key][5], ["", ""])[1]:{fields[8]}} │')
                elif i == 1:
                    print(f'│ {"":{fields[0]}} │ {db[0][key][i]:{fields[1]}} │ ' + ' │ '.join([f'{"":{fields[k + 2]}}' for k in range(5)]) + f' │ {db[1][key][i] + ",":{fields[7]}} │ {"":{fields[8]}} │')
                else:
                    print(f'│ {"":{fields[0]}} │ {db[0][key][i]:{fields[1]}} │ ' + ' │ '.join([f'{"":{fields[k + 2]}}' for k in range(5)]) + f' │ {db[1][key][i] + ", " + db[1][key][i+1]:{fields[7]}} │ {"":{fields[8]}} │')
        print_line('└', '┴', '┘', '─', fields)
    else:
        print_line('└', '┴', '┘', '─', fields)
        print('Работников пока нет')


def print_table(db, fields_name, fields, baze_name, size):
    print_header(fields_name, fields)
    if db:
        for key in size:
            print_line('├', '┼', '┤', '─', fields)
            print(f'│ {key:{fields[0]}} │ ' + ' │ '.join([f'{db[key][i]:{fields[i + 1]}}' for i in range(len(db[key]))]) + ' │')
        print_line('└', '┴', '┘', '─', fields)
    else:
        print_line('└', '┴', '┘', '─', fields)
        print(f'База "{baze_name}" пока пуста')
