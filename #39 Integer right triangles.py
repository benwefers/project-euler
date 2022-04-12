def gcd(a, b):
    while b > 0: a, b = b, a % b
    return a

# Based on Euclid's formula for Pythagorean triples
ps = [0] * 1001
for m in range(2, 22):
    for n in range(1, m):
        if m % 2 == 1 and n % 2 == 1 or gcd(n, m) != 1: continue
        p = 2 * m * (m + n)
        for k in range(1, 1000 // p + 1): ps[k * p] += 1
print(ps.index(max(ps)))