N = int(input())
for i in range(2, N+1):
    if N%i == 0:
        while N%i == 0:
            N //= i
            print(i)