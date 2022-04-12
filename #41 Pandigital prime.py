def isPrime(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0: return False
    return True

def permutations(a, l):
    if l == 0: yield ""
    else:
        for i, v in enumerate(a):
            for p in permutations(a[:i] + a[i + 1:], l - 1): yield v + p

m, d = 0, "987654321"
for l in range(9, 1, -1):
    for n in permutations(d[9 - l:], l):
        if isPrime(int(n)): m = int(n)
        if m != 0: break
    if m != 0: break
print(m)