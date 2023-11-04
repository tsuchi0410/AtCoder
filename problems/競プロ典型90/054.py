n,k=(int(x) for x in input().split())

l = [False] * 100000

for x in range(1, 100000):
    c = 0
    while x < 100000:
        y = 0
        for i in str(x):
            y += int(i)
        z = x + y
        x = z
        c += 1
        l[c] 