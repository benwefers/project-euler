def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)

s = 0
for n in range(3, 50000):
    if sum(factorial(int(d)) for d in str(n)) == n: s += n
print(s)