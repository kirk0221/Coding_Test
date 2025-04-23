def star(n):
    if n == 3:
        return print("***\n* *\n***", end = '')
    return star(n//3) * (n//3) + print() + star(n//3) + print(' ') * (n//3) + star(n//3) + star(n//3) * (n//3)

n = int(input())
star(n)