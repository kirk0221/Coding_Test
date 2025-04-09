n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
for i in range(n-1):
    for j in range(i,n):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
    print(l[i])
print(l[len(l)-1])