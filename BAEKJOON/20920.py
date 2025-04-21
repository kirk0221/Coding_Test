n, m = map(int, input().split())
dictionary = dict()
for _ in range(n):
    word = input()
    if len(word) < m:
        continue
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1
values = sorted(dictionary.values())
for i in range(len(values)-1, -1, -1):
    dictionary.values