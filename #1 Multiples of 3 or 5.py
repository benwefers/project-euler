def multiplesSum(n, m):
    mul = m // n
    return n * mul * (mul + 1) // 2

print(multiplesSum(3, 999) + multiplesSum(5, 999) - multiplesSum(15, 999))