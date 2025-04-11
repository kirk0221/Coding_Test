import sys
input = sys.stdin.readline
n, m = map(int, input().split())
set_n = set()
for _ in range(n):
    set_n.add(input())
count = 0
for _ in range(m):
    if input() in set_n:
        count+=1
print(count)