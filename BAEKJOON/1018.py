n, m = map(int, input().split())
ans = []
count_l = []

for _ in range(n):
    ans.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        count_w = 0
        count_b = 0
        color = ans[i][j]
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    if ans[k][l] != color:
                        count_b += 1
                    else:
                        count_w +=1
                else:
                    if ans[k][l] != color:
                        count_w += 1
                    else:
                        count_b+=1
        count_l.append(count_b)
        count_l.append(count_w)
        
print(min(count_l))
