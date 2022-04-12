def coinSum(s, coins):
    if len(coins) == 1: return 1
    c = 0
    for n in range(0, s // coins[0] + 1):
        c += coinSum(s - coins[0] * n, coins[1:])
    return c

print(coinSum(200, [200, 100, 50, 20, 10, 5, 2, 1]))