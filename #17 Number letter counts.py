def letterCount(n):
    olengths = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    tlengths = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
    if n < 20: return olengths[n]
    if n < 100: return tlengths[n // 10] + olengths[n % 10]
    if n % 100 == 0: return olengths[n // 100] + 7
    if n % 100 < 20: return olengths[n // 100] + 10 + olengths[n % 100]
    else: return olengths[n // 100] + 10 + tlengths[n % 100 // 10] + olengths[n % 10]

print(sum([letterCount(n) for n in range(1000)], 11))