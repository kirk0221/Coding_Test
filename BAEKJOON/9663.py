n = int(input())
batch = []
ans = [[0]*n for _ in range(n)]
count = 0

def queen(n):
    global count
    if len(batch) == 2 and ans[batch[0]][batch[1]] != 1:
        ans[batch[0]][batch[1]] = 1
        
        for i in range(n):
            ans[i][batch[1]] = 1
            ans[batch[0]][i] = 1
            if batch[0]+i < n and batch[1]+i < n:
                ans[batch[0]+i][batch[1]+i]
            if batch[0]-i >= 0 and batch[1]-i >= 0:
                ans[batch[0]-i][batch[1]-i]
        count+=1
        return
    elif len(batch) == 2: return
    for i in range(0, n):
        batch.append(i)
        queen(n)
        batch.pop()

queen(n)
print(ans)
print(count)