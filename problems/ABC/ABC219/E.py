from collections import deque

# 入力
H = 4
W = 4
S = [list(map(int, input().split())) for _ in range(H)]
house = set()
for i in range(H):
    for j in range(W):
        if S[i][j] == 1:
            house.add((i, j))

ans = 0
NUM = 16
for i in range(2 ** NUM):
    l = [i >> j & 1 for j in range(NUM)]
    G = [[0] * W for _ in range(H)]
    ii = 0
    start = []
    for j in range(len(l)):
        if j % 4 == 0 and j != 0:
            ii += 1
        if l[j] == 1:
            G[ii][j % 4] = 1
            start.append([ii, j % 4])

    d = [[-1] * W for _ in range(H)]
    loop = 0
    for sh, sw in start:
        if d[sh][sw] == -1:
            loop += 1 
            q = deque([[sh, sw]])
            while q:
                y, x = q.popleft()
                for i2, j2 in [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]:
                    
                    if i2 < 0 or j2 < 0:
                        continue
                    if i2 >= H or j2 >= W:
                        continue
                    
                    if d[i2][j2] == -1 and G[i2][j2] == 1:
                        q.append([i2, j2])
                        d[i2][j2] = d[y][x] + 1
            
    f = True
    for m, n in house:
        if d[m][n] == -1:
            f = False
    
    if f == True and loop == 1:
        fwall = False
        start = []
        for m in range(H):
            for n in range(W):
                if G[m][n] == 0 and 1 <= m <= 2 and 1 <= n <= 2:
                    start.append([m, n])
        
        if len(start) == 0:
            ans += 1
        else:
            for sh, sw in start:
                d = [[-1] * W for _ in range(H)]
                q = deque([[sh, sw]])
                while q:
                    y, x = q.popleft()
                    for i2, j2 in [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]:
                        
                        if i2 < 0 or j2 < 0:
                            continue
                        if i2 >= H or j2 >= W:
                            continue
                        
                        if d[i2][j2] == -1 and G[i2][j2] == 0:
                            q.append([i2, j2])
                            d[i2][j2] = d[y][x] + 1
                for y in range(H):
                    for x in range(W):
                        if y == 0:
                            if d[y][x] != -1:
                                fwall = True
                        if x == 0 or x == W - 1:
                            if d[y][x] != -1:
                                fwall = True
                        if y == H - 1:
                            if d[y][x] != -1:
                                fwall = True 
                if fwall == True:
                    ans += 1


print(ans)