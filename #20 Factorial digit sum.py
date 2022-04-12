f = 100
for i in range(1, 100):
    f *= i
print(sum(int(d) for d in str(f)))