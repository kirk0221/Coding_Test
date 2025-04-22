def recursion(s, l, r):
    recursion.counter+=1
    if(l>=r): return 1
    elif s[l]!=s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrom(s):
    recursion.counter = 0
    return recursion(s, 0, len(s)-1), recursion.counter

tc = int(input())
for _ in range(tc):
    s = input()
    ans, count = isPalindrom(s)
    print(ans, count)