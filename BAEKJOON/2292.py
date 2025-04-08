# 1, 1+6, 7+12, 19+18, 37+24...

# def beehive(N):
#     if N==1:
#         return 1
#     else:
#         return beehive(N-1) + 6*(N-1)

N = int(input())
count = 1
beehive = 1

while True:
    if N <= beehive:
        break
    beehive += 6 * count
    count += 1

print(count)