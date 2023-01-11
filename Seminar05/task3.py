# Задача 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_cod(a):
    res = ''
    pr = a[0]
    count = 1
    for i in range(1,len(a)):
        if a[i] == pr:
            count += 1
        else:
            res += str(count) + pr
            pr = a[i]
            count = 1
    return res + str(count) + pr


def rle_decod(a):
    res = ''
    pr = a[0]
    for i in range(1,len(a)):
        if a[i].isdigit():
            pr += a[i]
        else:
            res += a[i] * int(pr)
            pr = ''
    return res
        


with open('input.txt', 'r') as f:
    s1 = f.read()
with open('output.txt', 'w') as f:
    f.write(rle_cod(s1))
with open('output.txt', 'r') as f:
    s = f.read()
s2 = rle_decod(s)
if s1 == s2:
    print('Ok')
else:
    print('Error')