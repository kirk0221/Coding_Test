n, m = map(int, input().split())
l = []
for i in range(1,n+1):
    l.append(i)
for a in range(m):
    i, j = map(int, input().split())
    l[i-1], l[j-1] = l[j-1], l[i-1]
    
for k in l:
    print(k, end = ' ')