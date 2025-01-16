n, m = map(int, input().split())
b = [0]*n
for t in range(m):
    i, j, k = map(int, input().split())
    for a in range(i, j+1):
        b[a-1] = k
        
for i in b:
    print(i, end=' ')