N, M = map(int, input().split())
ans = []
save = []

def back(k):
    if len(ans) == M and ans not in save:
        save.append(set(ans))
        print(" ".join(map(str, ans)))
        return 
    for i in range(k, N+1):
        if i not in ans:
            ans.append(i)
            back(i)
            ans.pop()

back(1)