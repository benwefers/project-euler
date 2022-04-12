def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)

def getPermutiation(i, v):
    if len(v) == 1: return str(v[0])
    p = factorial(len(v) - 1)
    c = str(v.pop(i // p))
    return c + getPermutiation(i % p, v)

print(getPermutiation(999999, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))