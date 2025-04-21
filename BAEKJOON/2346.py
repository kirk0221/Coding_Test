from collections import deque
n = int(input())
l = list(map(int, input().split()))
deck = deque()
for i in range(len(l)):
    deck.append((i,l[i]))
while(deck):
    idx, num = deck.popleft()
    print(idx+1, end=' ')
    if num > 0:
        deck.rotate(-(num-1))
    elif num < 0:
        deck.rotate(-num)
