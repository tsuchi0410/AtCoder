from collections import deque

def bfs(ra,ca,rb,cb,h,w):
    
    q = deque([[ra, ca]])
    
    d = []
    for i in range(h):
        d.append([-1] * w)

    d[ra][ca] = 0

    while q:
        y, x = q.popleft()

        if y == rb and x == cb:
            s = 'Yes'
            return s
                
        for i, j in [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]:
            
            if i < 0 or j < 0:
                continue
            if i > h-1 or j > w-1:
                continue
            
            if d[i][j] == -1 and g[i][j] == True:
                q.append([i, j])
                d[i][j] = d[y][x] + 1
    
    s = 'No'
    return s

h, w = (int(x) for x in input().split())
g = [[False] * h for _ in range(w)]
q = int(input())
for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        r, c = query[1], query[2]
        g[r-1][c-1] = True
    else:
        ra, ca, rb, cb = query[1], query[2], query[3], query[4]
        ra -= 1; ca -= 1; rb -= 1; cb -= 1
        if g[ra][ca] == True and g[rb][cb] == True:
            s = bfs(ra,ca,rb,cb,h,w)
            print(s)
        else:
            print('No')