import sys
input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
num_l = list(map(int, input().split()))

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for num in num_l:
    result = count.get(num)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")