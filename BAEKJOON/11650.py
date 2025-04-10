n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

l.sort()

for i in range(n):
    print(l[i][0], l[i][1])

# 파이썬은 sort하면 2차원도 정렬된다..

# for i in range(n-1):
#     for j in range(i,n):
#         if l[i][1] > l[j][1]:
#             l[j][1], l[i][1] = l[i][1], l[j][1]
#         if l[i][0] > l[j][0]:
#             l[i][0], l[j][0] = l[j][0], l[i][0]
#     print(l[i][0], l[i][1])