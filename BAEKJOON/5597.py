l = []
for i in range(28):
    a = int(input())
    l.append(a)
for j in range(1,31):
    if j not in l:
        print(j)