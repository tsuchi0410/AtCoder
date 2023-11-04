from collections import deque

h, w = (int(x) for x in input().split())
x0, y0, x1, y1 = (int(x) for x in input().split())
s = [input() for _ in range(h)]

def bfs(y0, x0):
    
    q = deque([[y0, x0]])
    
    d = []
    for i in range(h):
        d.append([-1] * w)
    d[y0][x0] = 0
        
    while q:
        y, x = q.popleft()
    
        if y == x1 and x == y1:
            break
                
        for yi, xi in [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]:
            
            if xi < 0 or yi < 0:
                continue
            if yi >= h or xi >= w:
                continue
            
            if d[yi][xi] == -1:
                if s[yi][xi] == 'W':
                    q.append([yi, xi])
                    d[yi][xi] = d[y][x] + 1
                
    return d

a = bfs(y0, x0)
print(a[x1][y1])