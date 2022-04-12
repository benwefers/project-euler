def permutations(a, l):
    if l == 0: yield ""
    else:
        for i, v in enumerate(a):
            for p in permutations(a[:i] + a[i + 1:], l - 1): yield v + p

s, d = [1, 1], "123456789"
for o in permutations(d, 3):
    a, b = int(o[:2]), int(o[1:])
    if a / b == (a // 10) / (b % 10): s = [s[0] * a, s[1] * b]
print(s[1] // s[0])