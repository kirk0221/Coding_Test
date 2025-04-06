l = []
max_i, max_j = 0, 0
for i in range(9):
    l.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
        if l[i][j] > l[max_i][max_j]:
            max_i, max_j = i, j
print(l[max_i][max_j])
print(max_i + 1, max_j + 1)