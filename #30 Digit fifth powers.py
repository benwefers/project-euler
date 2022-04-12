s = 0
for i in range(2, 999999):
    if sum(int(n) ** 5 for n in str(i)) == i: s += i
print(s)