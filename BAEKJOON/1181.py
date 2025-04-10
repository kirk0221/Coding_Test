n = int(input())
l = []
s = set()
for _ in range(n):
    word = input()
    if word not in s:
        l.append(word)
        s.add(word)

l.sort(key=lambda x: (len(x), x))

for word in l:
    print(word)
