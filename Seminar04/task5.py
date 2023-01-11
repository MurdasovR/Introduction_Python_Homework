# Задача 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def polinom_read(file):
    with open(file, 'r') as f:
        a = f.read().split()
    i = 1
    while i < len(a):
        if (a[i] == '*' or a[i] == 'x' or a[i] == '+'):
            del a[i]
        elif (a[i] == '**'):
            del a[i]
            del a[i]
        elif (a[i] == '-'):
            del a[i]
            a[i] = '-' + a[i]
        else:
            i += 1
    return list(map(int, a))

def polinom_write(a):
    n = len(a)
    if n > 2:
        s = str(a[0]) + ' * x ** ' + str(n - 1)
        i = 1
        while i < n - 2:
            if (a[i] < 0):
                s += ' - ' + str(-a[i]) + ' * x ** ' + str(n - i - 1)
            else:
                s += ' + ' + str(a[i]) + ' * x ** ' + str(n - i - 1)
            i += 1
        for i in [n - 2, n - 1]:
            if (a[i] < 0):
                s += ' - ' + str(-a[i]) + (' * x' if i == n - 2 else '')
            else:
                s += ' + ' + str(a[i]) + (' * x' if i == n - 2 else '')             
    elif n == 2:
        s = str(a[0]) + ' * x' + (' - ' + str(-a[1])) if a[1] < 0 else (' + ' + str(a[1]))
    else:
        s = str(a[0])
    return s

def polinom_summa(a1, a2):
    len_max = max(len(a1), len (a2))
    p_summa = [0] * len_max
    dn = len(a1) - len (a2)
    for i in range (abs(dn)):
        if dn > 0:
            p_summa[i] = a1[i]
        elif dn < 0:
             p_summa[i] = a2[i]
        else:
            p_summa[i] = a1[i] + a2[i]
    for i in range (abs(dn), len_max):
        if dn > 0:
            p_summa[i] = a1[i] + a2[i - dn]
        else:
            p_summa[i] = a2[i] + a1[i + dn]
    return p_summa

 

with open('data3.txt', 'w') as f:
    f.write(polinom_write(polinom_summa(polinom_read('data1.txt'), polinom_read('data2.txt'))))