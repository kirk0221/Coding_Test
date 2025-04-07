n = int(input())
paper = [[0] * 100 for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

count = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] > 0:
            count += 1
print(count)