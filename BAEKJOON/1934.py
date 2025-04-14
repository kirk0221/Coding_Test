import math
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(math.lcm(a,b))


# 브루스 포트

# t = int(input())

# for _ in range(t):
#     a, b = map(int, input().split())
#     min_ab = min(a,b)
#     max_ab = max(a,b)
#     min_ab_add = min_ab
#     max_ab_add = max_ab
#     min_l = set()
#     max_l = set()
#     if min_ab == 1:
#         print(max_ab)
#     else:
#         while(True):
#             min_l.add(min_ab)
#             max_l.add(max_ab)
#             if min_l.intersection(max_l):
#                 break 
#             min_ab += min_ab_add
#             max_ab += max_ab_add
#         print(min_l.intersection(max_l).pop())    