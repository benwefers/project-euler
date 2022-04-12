def smallestMultiple(n):
    nums = range(1, n)
    p = 1
    for i in range(n - 1):
        a = nums[i]
        p *= a
        nums = [num // a if num % a == 0 else num for num in nums]
    return p

print(smallestMultiple(20))