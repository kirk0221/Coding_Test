n, m = map(int, input().split())
l = [i for i in range(1,n+1)]
for k in range(m):
    i, j = map(int, input().split())
    temp = l[i-1:j]
    temp.reverse()
    l[i-1:j]= temp

for i in range(n):
    print(l[i], end = ' ')
        