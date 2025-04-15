import math
import sys
input= sys.stdin.readline
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

l.sort()
gap = []
for i in range(n-1):
    gap.append(l[i+1] - l[i])

gcd = math.gcd(*gap)

count = 0
for g in gap:
    count += g // gcd -1 #  gap 안에 들어갈 수 있는 수의 개수를 gap // gcd - 1로 바로 계산.
print(count)

# for i in range(l[0], l[-1], gcd): 
#     if i not in l: # in 연산은 리스트에서 O(n) 시간이 걸림 (리스트 탐색).
#         count+=1