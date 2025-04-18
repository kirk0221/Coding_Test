from collections import deque
n = int(input())
deck = deque(map(int, input().split()))
idx = 0
count = 1
ans = [0]*n
while(deck):
    num = deck.popleft()
    ans[idx] = count
    if num > 0:
        for i in range(num):
            deck.append(deck.popleft())
            idx+=1
    elif num < 0:
        for i in range(num, 0, -1):
            deck.appendleft(deck.pop())
            idx-=1
    idx %= n
    count+=1
print(ans)

