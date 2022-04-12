m = 0
for a in range(10 ** 3 - 1, 10 ** 2, -1):
    for b in range(a, 10 ** 2, -1):
        if str(a * b) == str(a * b)[::-1] and a * b > m: m = a * b
print(m)