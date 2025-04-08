N = int(input())
# 2, 2+1, 2+2, 5+4, 9+8
result = 0
def dot(N):
    if N == 0:
        return 2
    else:
        return dot(N-1) + 2 ** (N-1)
result = dot(N)
print(result**2)