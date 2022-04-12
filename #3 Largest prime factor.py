def largestFactor(n):
    f = 2
    while f < n:
        while n % f == 0: n = n // f
        f += 1
    return f
    
print(largestFactor(13195))