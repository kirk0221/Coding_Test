tc = int(input())
for _ in range(tc):
    s = []
    t = list(input())
    ans = "YES"
    while t:
        word = t.pop()
        if word == ')':
            s.append(word)
        else:
            if s:
                s.pop()
            else:
                ans = "NO"
                break
    if s:
        ans = "NO"
    print(ans)
    
    