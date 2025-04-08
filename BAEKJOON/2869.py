import math
A, B, V = map(int, input().split())
print(math.ceil((V-A)/(A-B))+1)

# height = 0
# count = 0
# while True:
#     height += A
#     count += 1
#     if height >= V:
#         break
#     height -= B
# print(count)