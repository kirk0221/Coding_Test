import sys
input = sys.stdin.readline
n = int(input())
l = []
count = dict()
for _ in range(n):
    num = int(input())
    l.append(num)
    if num not in count:
        count[num] = 1
    else:
        count[num] += 1
print(round(sum(l)/len(l)))
l.sort()
print(l[len(l)//2])
freq = max(count.values())
numbers = []
for key, value in count.items():
    if value == freq:
        numbers.append(key)

if len(numbers) == 1:
    print(numbers[0])
else:
    print(sorted(numbers)[1])
print(max(l) - min(l))