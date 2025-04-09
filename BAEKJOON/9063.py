n = int(input())
lx = []
ly = []
for i in range(n):
    x, y = map(int, input().split())
    lx.append(x)
    ly.append(y)

print((max(lx) - min(lx)) * (max(ly) - min(ly)))