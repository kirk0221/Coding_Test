n, m = map(int, input().split())
l = list(map(int, input().split()))
max = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            now = l[i] + l[j] + l[k]
            if now <= m and max < now:
                max = now
print(max)