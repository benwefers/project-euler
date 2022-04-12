names = open("Assets/#22 names.txt").readline()
names = sorted(names.replace("\"", "").split(","))
t = 0
for i in range(len(names)):
    s = sum(ord(c) - 64 for c in names[i])
    t += s * (i + 1)
print(t)