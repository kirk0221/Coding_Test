check = [0] * 2 + [1] * 1000000

for i in range(2, 1000000):
    if check[i]:
        for j in range(i * 2, 1000000, i):
            check[j] = 0

tc = int(input())
for _ in range(tc):
    n = int(input())
    count = 0
    for i in range(2, int(n/2)+1):
        if check[i] == 1 and check[n-i] == 1:
            count+=1
    print(count)

'''
6 = 3+3
8 = 3+5
10 = 3+7, 5+5
12 = 5+7

'''