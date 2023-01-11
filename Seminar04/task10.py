d = dict()
string = input()
while string !='':
    di = string.split()
    if di[0] not in d.keys():
        d[di[0]] = {di[1]}
    else:
        d[di[0]].add(di[1])
    if di[1] not in d.keys():
        d[di[1]] = {di[0]}
    else:
        d[di[1]].add(di[0])
    string = input()
d_res = {i: set() for i in d.keys()}
for i in d.keys():
    for j in d[i]:
        temp = d[j].copy()
        temp.discard(i)
        temp.difference_update(d[i]) 
        d_res[i] = d_res[i].union(temp)
for i in sorted(d_res):
    print(f'{i}: {", ".join(sorted(d_res[i]))}')

