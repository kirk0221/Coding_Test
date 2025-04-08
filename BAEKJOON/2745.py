import string
N, B = input().split()
B = int(B)
N = list(N)
result = 0
for i in range(len(N), 0, -1):
    if N[i-1] in string.ascii_uppercase:
        result += (ord(N[i-1]) - 55) * (B ** (len(N) - i))
    elif N[i-1] in string.digits:
        result += int(N[i-1]) * (B ** (len(N) - i))
print(result)
