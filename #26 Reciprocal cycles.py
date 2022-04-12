def cycleLength(d):
    s = []
    n = 10
    for i in range(d):
        if n == 0: return 0
        if n in s: return i - s.index(n)
        s.append(n)
        n = (n % d) * 10

c, n = max((cycleLength(i), i) for i in range(2, 1000))
print(n)