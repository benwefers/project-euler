def permutations(a, l):
    if l == 0: yield ""
    else:
        for i, v in enumerate(a):
            for p in permutations(a[:i] + a[i + 1:], l - 1): yield v + p

l, d = set(), "123456789"
for o in permutations(d, 5):
    for i in range(2):
        a, b = int(o[:1 + i]), int(o[1 + i:5])
        p = str(a * b)
        if len(p) == 4 and set(p) == set(d) - set(o): l.add(a * b)

print(sum(l))