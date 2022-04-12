def Champernowne(n):
    n, d, b = n - 1, 1, 9
    while n > b: n, d, b = n - b, d + 1, (d + 1) * 9 * 10 ** (d)
    return int(str(n // d + 10 ** (d - 1))[n % d])

p = 1
for i in range(7): p *= Champernowne(10 ** i)
print(p)