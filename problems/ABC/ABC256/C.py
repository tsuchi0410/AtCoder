l = list(map(int,input().split()))

ans = 0
for a in range(1, 31):
    for b in range(1, 31):
        for d in range(1, 31):
            for e in range(1, 31):
                c = l[0] - a - b
                f = l[1] - d - e
                g = l[3] - a - d
                h = l[4] - b - e
                i1 = l[5] - c - f
                i2 = l[2] - g - h

                if min(c, f, g, h, i1, i2) > 0 and i1 == i2:
                    ans += 1


print(ans)