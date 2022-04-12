def nthPrime(n):
    primes = [2]
    i = 3
    while len(primes) <= n:
        prime = True
        for p in primes:
            if i % p == 0: prime = False
            if p >= int(i ** 0.5) or not prime: break
        if prime: primes.append(i)
        i += 2
    return primes[n - 1]

print(nthPrime(10001))