l = set()
for i in range(10):
    a = int(input())
    a%=42
    l.add(a)
print(len(l))