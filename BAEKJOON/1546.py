n = int(input())
l = list(map(int, input().split()))
m = max(l)
avg = 0
for i in l:
    i = i/m * 100
    avg += i
print(avg/n)