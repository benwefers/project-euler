def prod(l):
    p = 1
    for n in l: p *= n
    return p

grid = open("Assets/#11 grid.txt").readlines()
grid = [[int(n) for n in row.split()] for row in grid]
m = 0
r = len(grid)
c = len(grid[0])
for i in range(r):
    for j in range(c):
        ds = prod([grid[i + k][j] for k in range(min(4, r - i))])
        rs = prod([grid[i][j + k] for k in range(min(4, c - j))])
        dd = prod([grid[i + k][j + k] for k in range(min(4, r - i, c - j))])
        ud = prod([grid[i - k][j + k] for k in range(min(4, i, c - j))])
        if max(ds, rs, dd, ud) > m: m = max(ds, rs, dd, ud)
print(m)