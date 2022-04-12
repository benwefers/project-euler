s = set()
for a in range(2, 101):
    s.update([a ** b for b in range(2, 101)])
print(len(s))