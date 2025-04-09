n = int(input())
count = 0
num = 666
while True:
    l = list(str(num))
    for i in range(1, len(l)-1):
        if l[i-1] == '6' and l[i] =='6' and l[i+1] == '6':
            count+=1
            break
    if count == n:
        print(num)
        break
    num+=1