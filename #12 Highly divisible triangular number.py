i = 0
while True:
    i += 1
    c = 0
    n = i * (i + 1) // 2
    for f in range(1, int(n ** 0.5)):
        if n % f == 0: c += 2
    if c > 500: break
print(n)