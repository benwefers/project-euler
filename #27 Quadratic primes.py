def primeSieve(n):
    sieve = [False] * 2 + [True] + [i % 2 == 0 for i in range(n - 2)]
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]: sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return sieve

ma = mb = mn = 0
ps = primeSieve(20000)
pv = [i for i in range(2000) if ps[i]]
for b in [i for i in pv if i < 1000]:
    for a in [i - b - 1 for i in pv if abs(i - b - 1) < 1000]:
        n = 0
        while ps[n ** 2 + a * n + b]: n += 1
        if n > mn: ma, mb, mn = a, b, n
print(ma * mb)