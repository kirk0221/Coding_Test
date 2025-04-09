n = int(input())
ans = 0
while True:
    if ans == n:
        print(0)
        break
    l = list(str(ans))
    sum = ans
    for num in l:
        sum+=int(num)
    if sum == n:
        print(ans)
        break
    ans+=1