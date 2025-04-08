N, B = map(int, input().split())
result = []
while N > 0:
    temp = N % B
    N //= B
    if B > 10:
        if temp >= 10:
            result.append(chr(temp + 55))
        else:
            result.append(str(temp))
    else:
        result.append(str(temp))

result.reverse()
print(''.join(result))
