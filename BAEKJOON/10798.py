l = []
for i in range(5):
    l.append(list(map(str, input().strip())))
    for j in range(len(l[i]), 15):
        l[i].append('')
for i in range(len(l[i])):
    for j in range(5):
        print(l[j][i], end='')