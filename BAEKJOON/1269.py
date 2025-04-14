a, b = map(int, input().split())

s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

s3 = s1.intersection(s2)

print(a+b-2*len(s3))