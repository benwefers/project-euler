s = 0
for n in range(1000000):
    if str(n) == str(n)[::-1] and bin(n)[2:] == bin(n)[2:][::-1]: s += n
print(s)