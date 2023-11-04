h,w = (int(x) for x in input().split())
g = []
for i in range(h):
    g.append(list(map(int,input().split())))

check = []
for i in range(h):
    l = []
    for j in range(w):
        l2 = []
        for y, x in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
            if y < 0 or x < 0 or y >= h or x >= w:
                l2.append(None)
                continue
            if g[y][x] == 0:
                l2.append(0)
            if g[y][x] == 1:
                l2.append(1)
        l.append(l2)
    check.append(l)

idx_h = []
for i in range(h):
    f = 0
    for j in range(w):
        cnt0 = 0
        cnt1 = 0
        for k in range(4):
            if g[i][j][k] == 0:
                cnt0 += 1
            elif g[i][j][k] == 1:
                cnt1 += 1
        if cnt0 == 0 or cnt1 == 0:
            f = 1
    if f == 1:
        idx_h.append(i)

if len(idx_h) == 0:
    print(0)
    exit()


for i in range(len(idx_h)):
    
    for j in range(w):
        check[idx_h[0] - 1][j][1] = 1 - check[idx_h[0] - 1][j][1]
        check[idx_h[0] + 1][j][1] = 1 - check[idx_h[0] + 1][j][1]

    f = 0
    for j in range(w):
        cnt0 = 0
        cnt1 = 0
        for k in range(4):
            if g[i][j][k] == 0:
                cnt0 += 1
            elif g[i][j][k] == 1:
                cnt1 += 1
        if cnt0 == 0 or cnt1 == 0:
            print(-1)