n = int(input())

l = []
for i in range(n):
    a, b = input().split()
    l.append([int(a), b])

l.sort(key=lambda x : x[0])

for i in range(n):
    print(l[i][0], l[i][1])