x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 != x2 and x1 != x3:
    x4 = x1
if x2 != x1 and x2 != x3:
    x4 = x2
if x3 != x1 and x3 != x2:
    x4  = x3
if y1 != y2 and y1 != y3:
    y4 = y1
if y2 != y1 and y2 != y3:
    y4 = y2
if y3 != y1 and y3 != y2:
    y4  = y3
print(x4, y4)