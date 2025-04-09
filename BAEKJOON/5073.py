while True:
    a, b, c = map(int, input().split())

    if (a == b == c == 0):
        break
    if ((a+b+c - max(a,b,c)) > max(a,b,c)):
        if (a == b == c):
            print("Equilateral")
        elif (a != b and b != c and c != a):
            print("Scalene")
        else:
            print("Isosceles")
    else:
        print("Invalid")