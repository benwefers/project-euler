n = open("Assets/#8 series.txt").readlines()
n = "".join(n).replace("\n", "")
m = 0
for i in range(len(n) - 1):
    p = 1
    for d in n[i:i + 13]:
        p *= int(d)
    if p > m: m = p
print(m)