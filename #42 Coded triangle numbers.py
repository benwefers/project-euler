words = open("Assets/#42 words.txt").readline()
words = words.replace("\"", "").split(",")
c = 0
for i in range(len(words)):
    n = sum(ord(c) - 64 for c in words[i])
    if (((1 + 8 * n) ** 0.5 - 1) / 2).is_integer(): c += 1
print(c)