n =  int(input())
ticket = list(map(int, input().split()))
s = []
count = 1
for i in range(n):
    if count == n:
        break
    elif ticket[i] == count:
        count += 1
    elif ticket[i]> count:
        s.append(ticket[i])
    while (s and s[-1] == count):
        if s[-1] == count:
            s.pop()
            count += 1
if s:
    print("Sad")
else:
    print("Nice")
