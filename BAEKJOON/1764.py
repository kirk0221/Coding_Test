n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.add(input())
l = []
for _ in range(m):
    name = input()
    if name in s:
        l.append(name)
l.sort()
print(len(l))
for name in l:
    print(name)
