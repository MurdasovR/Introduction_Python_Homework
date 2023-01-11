# Калькулятор

def sel_terms(string):
    string = ''.join(string.split()).lower()
    string = string.replace(',', '.')
    string = string.replace('(', '')
    string = string.replace(')', '')
    all_operation = '*/+-'
    operation = ''
    term = [''] * 2
    if (0 < string.find('j') < len(string) - 1) and string[string.find('j') + 1] in all_operation:
        operation = string[string.find('j') + 1]
        term[0] = string[0:string.find('j') + 1]
        term[1] = string[string.find('j') + 2:]
    else:
        index_operation = 0
        while operation == '' and index_operation < 4:
            if string[0] == '-' and len(string[1:].split(all_operation[index_operation], 1)) == 2:
                operation = all_operation[index_operation]
                for i in range(2):
                    term[i] = string[1:].split(all_operation[index_operation], 1)[i]
                term[0] = '-' + term[0]
            elif string[0] != '-' and len(string.split(all_operation[index_operation], 1)) == 2:
                operation = all_operation[index_operation]
                for i in range(2):
                    term[i] = string.split(all_operation[index_operation], 1)[i]
            else:
                index_operation += 1
    if '' in [operation] + term:
        return 0
    else:
        type_terms = [''] * 2
        for i in [0, 1]:
            flag = 1
            try:
                test = int(term[i])
            except:
                flag = 0
            if flag == 1:
                type_terms[i] = int
            else:
                flag = 1
                try:
                    test = float(term[i])
                except:
                    flag = 0
                if flag == 1:
                    type_terms[i] = float
                else:
                    flag = 1
                    try:
                        test = complex(term[i])
                    except:
                        flag = 0
                    if flag == 1:
                        type_terms[i] = complex
                    else:
                        return 0
        return [operation] + term + type_terms


def calc(terms):
    flag = 1
    match terms[0]:
        case '+':
            result = terms[3](terms[1]) + terms[4](terms[2])
        case '-':
            result = terms[3](terms[1]) - terms[4](terms[2])
        case '*':
            result = terms[3](terms[1]) * terms[4](terms[2])
        case '/':
            try:
                result = terms[3](terms[1]) / terms[4](terms[2])
            except:
                flag = 0
    if flag:
        result = f'{terms[3](terms[1])} {terms[0]} {terms[4](terms[2])} = {result}'
    else:
        result = f'Ошибка деления! Число {terms[3](terms[1])} нельзя поделить на {terms[4](terms[2])}!'
    return result