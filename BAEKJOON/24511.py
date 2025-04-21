from collections import deque

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))


queue = deque()
for i in range(n):
    if a[i] == 0:
        queue.appendleft(b[i])

for i in range(m):
    queue.append(c[i])
    print(queue.popleft(), end = ' ')



''' 큐 스택 스택 큐
1 2 3 4
2 2 3 1 ... 4

'''