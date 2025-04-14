s = input()
ans_set = set()
for i in range(len(s)+1):
    for j in range(i, len(s)+1):
        ans_set.add(s[i:j])
print(len(ans_set)-1)