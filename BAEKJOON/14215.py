a, b, c = map(int, input().split())

while True:
    if (a+b+c - max(a,b,c)) > max(a,b,c):
        print(a+b+c)
        break
    if a == max(a,b,c):
        a-=1
    elif b == max(a,b,c):
        b-=1
    elif c == max(a,b,c):
        c-=1