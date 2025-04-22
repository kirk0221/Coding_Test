import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
dictionary = dict()
for _ in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1
values = sorted(dictionary.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
for i in range(len(values)):
    print(values[i][0])