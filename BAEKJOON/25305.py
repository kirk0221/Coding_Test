n, k = map(int, input().split())
x = list(map(int, input().split()))
for i in range(n):
    for j in range(i+1, n):
        if x[i] < x[j]:
            x[i], x[j] = x[j], x[i]
print(x[k-1])