def d(n):
    s = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: s += i + n // i if n // i != i else i
    return s

a = [False] * 28125
s = a.copy()
for n in range(1, len(a)):
    if n < d(n):
        a[n] = True
        for i in [n for n in range(len(s) - n) if a[n]]:
            s[n + i] = True
print(sum([n for n in range(len(s)) if not s[n]]))