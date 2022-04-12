def latticePaths(n):
    c = 1
    for i in range(1, n + 1):
        c = c * (n + i) // i
    return c
    
print(latticePaths(20))