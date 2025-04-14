import math
a, b = map(int, input().split())
c, d = map(int, input().split())

qnswk = a*d + c*b
qnsah = b*d
g = math.gcd(qnswk, qnsah)

print(int(qnswk/g), int(qnsah/g))