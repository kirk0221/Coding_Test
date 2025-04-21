n, k =  map(int, input().split())
ans = 1
for i in range(n+1-k, n+1):
    ans*=i
for j in range(1,k+1):
    ans/=j
print(int(ans))