# 1/1 : 1
# 1/2 2/1 : 3
# 3/1 2/2 1/3 : 6
# 1/4 2/3 3/2 4/1 : 10
# 5/1 4/2 3/3 2/4 1/5 : 15
# ...
X = int(input())
count = 1
plus = 2
line = 1
while True:
    if count >= X:
        break
    count += plus
    plus += 1
    line += 1
if line % 2 == 0:
    den = count - X + 1
    num = line - den + 1
else:

    num = count - X + 1
    den = line - num + 1
print(f"{num}/{den}")