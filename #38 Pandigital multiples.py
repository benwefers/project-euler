def permutations(a, l):
    if l == 0: yield ""
    else:
        for i, v in enumerate(a):
            for p in permutations(a[:i] + a[i + 1:], l - 1): yield v + p

m, d = 0, "123456789"
for l in range(2, 5):
    for n in permutations(d, l):
        s, i = n, 2
        while len(s) < 9: s, i = s + str(int(n) * i), i + 1
        if len(s) == 9 and set(s) == set(d): m = max(m, int(s))
print(m)