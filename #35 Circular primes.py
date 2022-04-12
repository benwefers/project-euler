def primeSieve(n):
    sieve = [False] * 2 + [True] + [i % 2 == 0 for i in range(n - 2)]
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]: sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return sieve

def rotations(n):
    s = str(n)
    for r in range(len(s)):
        yield int(s)
        s = s[1:] + s[0]

c = 0
ps = primeSieve(1000000)
for n in range(1000000):
    if sum(not ps[r] for r in rotations(n)) == 0: c += 1
print(c)