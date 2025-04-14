n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
gap = 1000000000
for i in range(len(l)-1):
    temp = l[i+1] - l[i]
    if temp < gap:
        gap = temp
while True:
    l_copy = l.copy()
    count = 0
    for i in range(l_copy[0], l_copy[-1]+1, gap):
        if i in l:
            l_copy.pop(0)
            count+=1
    if len(l_copy) == 0:
        break
    gap/=gap
    gap = int(gap)
print(count)



# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(input()))
# l.sort()
# gap = 1000000000
# for i in range(len(l)-1):
#     temp = l[i+1] - l[i]
#     if temp < gap:
#         gap = temp
