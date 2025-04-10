n = int(input())
l = []
for _ in range(n):
    a, b = (map(int, input().split()))
    l.append([b,a])

l.sort()
#l.sort(key = lambda x : (x[1], x[0]))

for i in range(n):
    print(l[i][1], l[i][0])