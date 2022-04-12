def primeSieve(n):
    sieve = [False] * 2 + [True] + [i % 2 == 0 for i in range(n - 2)]
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]: sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return sieve

def truncations(n):
    s = str(n)
    yield(n)
    for i in range(1, len(s)): yield int(s[i:])
    for i in range(1, len(s)): yield int(s[:i])

s = 0
ps = primeSieve(750000)
for n in range(8, 750000):
    if sum(not ps[t] for t in truncations(n)) == 0: s += n
print(s)