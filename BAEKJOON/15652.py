N, M = map(int, input().split())
ans = []

def back(k):
    if len(ans) == M :
        print(" ".join(map(str, ans)))
        return 
    for i in range(k, N+1):
        ans.append(i)
        back(i)
        ans.pop()

back(1)