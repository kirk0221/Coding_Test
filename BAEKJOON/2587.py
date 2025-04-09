l = []
sum = 0
for _ in range(5):
    num = int(input())
    l.append(num)
    sum += num
for i in range(4):
    for j in range(i+1, 5):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(int(sum/5))
print(l[2])