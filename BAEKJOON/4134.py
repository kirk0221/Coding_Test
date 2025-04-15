# import sys
# input = sys.stdin.readline
# tc = int(input())
# for _ in range(tc):
#     n = int(input())
#     flag = True
#     while flag:
#         if n==0 or n==1:
#             n = 2
#             break
#         for i in range(2, int(n**0.5)+1):
#             if n%i == 0:
#                 n+=1
#                 flag = True
#                 break
#             else:
#                 flag = False
#     print(n)

import sys
input = sys.stdin.readline

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

tc = int(input())
for _ in range(tc):
    n = int(input())
    while not is_prime(n):
        n += 1
    print(n)