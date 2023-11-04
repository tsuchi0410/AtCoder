from collections import deque
import math
n, m = (int(x) for x in input().split())

def bfs(v, d):
    
    q = deque([[0, 0]])
    
    while q:
        y, x = q.popleft()

        for a in range(len(v)):
            for i, j in [[y + v[a][0], x + v[a][1]], [y + v[a][0], x - v[a][1]], [y - v[a][0], x + v[a][1]], [y - v[a][0], x - v[a][1]]]:
                
                if i < 0 or j < 0:
                    continue
                if i >= n or j >= n:
                    continue
            
                if d[i][j] == -1:
                    d[i][j] = d[y][x] + 1
                    q.append([i, j])
                
    return d

k = int(math.sqrt(m))
v = []
for i in range(k+1):
    for j in range(k+1):
        
        if i**2 + j**2 == m:
            v.append([i, j])
d = []
for i in range(n):
    d.append([-1] * n)
d[0][0] = 0

a = bfs(v, d)

for i in d:
    print(*i, sep=' ')