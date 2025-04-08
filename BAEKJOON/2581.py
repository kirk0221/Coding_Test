M = int(input())
N = int(input())

l = []
for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        l.append(i)
if len(l) == 0:
    print(-1)
else:
    print(sum(l))
    print(l[0])