import sys
input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
    order = input().split()
    if order[0] == '1':
        l.append(int(order[1]))
    elif order[0] == '2':
        if l:
            print(l.pop())
        else:
            print(-1)
    elif order[0] == '3':
        print(len(l))
    elif order[0] == '4':
        if l:
            print(0)
        else:
            print(1)
    elif order[0] == '5':
        if l:
            print(l[-1])
        else:
            print(-1)