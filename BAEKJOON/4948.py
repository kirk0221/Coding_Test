while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    n2 = 2*n
    for i in range(n+1, n2+1, 1):
        if n2%i != 0:
            count+=1
    print(count)