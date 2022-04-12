def day(d, m, y):
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    b = d + sum(months[0:m - 1]) + y * 365
    if m >= 2: y -= 1
    return b + y // 4 - y // 100 + y // 400

c = 0
sunday = day(1, 1, 1900) - 1
for y in range(1901, 2001):
    for m in range(1, 13):
        if (day(1, m, y) - sunday) % 7 == 0: c += 1
print(c)