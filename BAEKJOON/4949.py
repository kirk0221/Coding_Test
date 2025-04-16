import sys

input = sys.stdin.readline

flag = True
while flag:
    s = []
    flag2 = False
    string = list(input())
    if string == ['.','\n']:
        break
    for word in string:
        if word == ")":
            if s:
                if s.pop() != "(":
                    flag2 = True
                    break
            else:
                flag2 = True
                break
        elif word == "]":
            if s:
                if s.pop() != "[":
                    flag2 = True
                    break
            else:
                flag2 = True
                break
        elif word == "(" or word == "[":
            s.append(word)
    if s and flag2:
        print("no")
    else:
        print("yes")