import math
tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    print(math.comb(m,n))
    

'''
case
3 5

1-1
2-2
3-3,4,5

1-1
2-3
3-4,5

1-1
2-4
3-5

1-2
2-3
3-4,5

1-2
2-4
3-5

1-3
2-4
3-5

==> 3! + 2!+ + 1!

case
2 5

1-1
2-2,3,4,5

1-2
2-3,4,5

1-3
2-4,5

1-4
2-5

==> 5+4+3+2+1

case
4 7

1-1
2-2
3-3
4-4,5,6,7

1-1
2-3
3-4
4-5,6,7

1-1
2-4
3-5
4-6,7

1-1
2-5
3-6
4-7

1-2
2-3
3-4
4-5,6,7

1-2
2-4
3-5
4-6,7

1-2
2-5
3-6
4-7

1-3
2-4
3-5
4-6,7

1-3
2-5
3-6
4-7

1-4
2-5
3-6
4-7

==> 4!+3!+2!+1!
'''