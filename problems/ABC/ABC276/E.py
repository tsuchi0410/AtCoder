from collections import deque
vec = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(y, x):
    
    q = deque([[y, x]])
    d = [[-1] * w for _ in range(h)]
    d[y][x] = 0

    while q:
        y, x = q.popleft()
                
        for v in vec:
            i = y + v[0]; j = x + v[1]
            if i < 0 or j < 0:
                continue
            if i >= h or j >= w:
                continue
            if d[i][j] == -1 and c[i][j] == '.':
                q.append([i, j])
                d[i][j] = d[y][x] + 1
    return d
                

h, w = (int(x) for x in input().split())
c = [input() for _ in range(h)]

# スタート地点
for i in range(h):
    for j in range(w):
        if c[i][j] == 'S':
            si , sj = i, j

# 判定（上下左右４マス）
l = []
for v in vec:
    i = si + v[0]; j = sj + v[1]
    if i < 0 or j < 0:
        continue
    if i >= h or j >= w:
        continue
    if c[i][j] == '.': 
        l.append([i, j])

for y, x in l:
    g = bfs(y, x)
    for v in vec:
        i = si + v[0]; j = sj + v[1]
        if i < 0 or j < 0:
            continue
        if i >= h or j >= w:
            continue
        if g[i][j] >= 2:
            print('Yes')
            exit()
            
print('No')