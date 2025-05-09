def hanoi(first, middle, last):
    if first==1:
        print(middle, last)
        return
    hanoi(first-1, middle, 6-middle-last)
    print(middle, last)
    hanoi(first-1, 6-middle-last, last)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3)

'''
하노이 규칙

100
200
300

000
200
301

000
000
321

000
010
320

000
010
023

000
000
123

000
002
103

001
002
003


print(1, 3)
print(1, 2)
print(3, 2)
print(1, 3)
print(2, 1)
print(2, 3)
print(1, 3)
'''