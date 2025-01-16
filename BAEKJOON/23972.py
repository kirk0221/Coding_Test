k,n=map(int, input().split())
if n == 1:
    print(-1)
else:
    x=(n*k)//(n-1)
    if (n*k)%(n-1): 
        print(x+1)
    else:
        print(x)