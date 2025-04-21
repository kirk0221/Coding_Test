n = int(input())
dance_set = set()
for _ in range(n):
    a, b = input().split()
    if a == "ChongChong" or b == "ChongChong" or a in dance_set or b in dance_set:
        dance_set.add(a)
        dance_set.add(b)
print(len(dance_set))