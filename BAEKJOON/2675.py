t = int(input())
for i in range(t):
    r, s = input().split()
    for k in s:
        for j in range(int(r)):
            print(k, end = '')
    print()