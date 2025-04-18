import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
deck = deque()
for _ in range(n):
    order = input().split()
    if order[0] == '1':
        deck.appendleft(order[1])
    elif order[0] == '2':
        deck.append(order[1])
    elif order[0] == '3':
        if deck:
            print(deck.popleft())
        else:
            print(-1)
    elif order[0] == '4':
        if deck:
            print(deck.pop())
        else:
            print(-1)
    elif order[0] == '5':
        print(len(deck))
    elif order[0] == '6':
        if deck:
            print(0)
        else:
            print(1)
    elif order[0] == '7':
        if deck:
            print(deck[0])
        else:
            print(-1)
    elif order[0] == '8':
        if deck:
            print(deck[-1])
        else:
            print(-1)