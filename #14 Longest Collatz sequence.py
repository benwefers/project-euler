def collatz(n):
    while n != 1:
        yield n
        if n % 2 == 0: n = n // 2
        else: n = 3 * n + 1
    yield n

found = {}
mn = ml = 0
for n in range(1, 1000000):
    l = 0
    steps = []
    for i in collatz(n):
        if i in found:
            l += found[i]
            break
        steps.append(i)
        found[i] = -l
        l += 1
    for s in steps: found[s] += l
    if l > ml:
        ml, mn = l, n
print(mn)