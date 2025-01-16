H, M = map(int, input().split())
T = int(input())
a = M+T

H+=a//60
M=a%60
H=H%24

print(H, M)