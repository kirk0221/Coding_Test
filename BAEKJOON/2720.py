T = int(input())
for _ in range(T):
    C = int(input())
    coins = [25, 10, 5, 1]
    result = []
    for coin in coins:
        result.append(C // coin)
        C %= coin
    print(' '.join(map(str, result)))