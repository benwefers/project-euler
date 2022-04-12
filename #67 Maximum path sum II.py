p = open("Assets/#67 pyramid.txt").readlines()
p = [[int(n) for n in row.split()] for row in p]
for i in range(len(p) - 2, -1, -1):
        for j in range(len(p[i])):
            p[i][j] += max(p[i + 1][j], p[i + 1][j + 1])
print(p[0][0])