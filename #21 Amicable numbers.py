def d(n):
    s = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: s += i + n // i if n // i != i else i
    return s

s = 0
for i in range(1, 10000):
    v = d(i)
    if d(v) == i and v != i: s += i
print(s)