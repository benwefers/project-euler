c = d = "0123456789"
for p in [1, 17, 13, 11, 7, 5, 3, 2, 1]:
    c = [b + a for a in c for b in d if int((b + a)[:3]) % p == 0 and b not in a]
print(sum([int(n) for n in c]))


# Brute Force
exit()
def permutations(a, l):
    if l == 0: yield ""
    else:
        for i, v in enumerate(a):
            for p in permutations(a[:i] + a[i + 1:], l - 1): yield v + p

s, d, p = 0, "0123456789", [1, 2, 3, 5, 7, 11, 13, 17]
for n in permutations(d, 10):
    f = False
    for i in range(8):
        f = int(n[i: i + 3]) % p[i] != 0
        if f: break
    if not f: s += int(n)
print(s)