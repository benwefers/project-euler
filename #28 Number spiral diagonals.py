s, v = 1, 1
for l in range(1, (1001 + 1) // 2):
    for c in range(4):
        v += 2 * l
        s += v
print(s)