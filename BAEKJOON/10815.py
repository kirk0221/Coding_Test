import sys
input = sys.stdin.readline
n = int(input())
card = set(map(int, input().split()))
m = int(input())
num_l = list(map(int, input().split()))

for i in num_l:
    if i in card:
        print(1, end= ' ')
    else:
        print(0, end= ' ')
    