from collections import deque
n, k = map(int, input().split())
queue = deque()
ans = []
for i in range(1, n+1):
    queue.append(i)
while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())
print("<", end='')
for i in range(n-1):
    print(ans[i], end = ', ')
print(ans[-1], end = '')
print(">")