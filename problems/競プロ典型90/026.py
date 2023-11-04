from collections import deque

def bfs(u):
    
    queue = deque([u])
    color[u] = 0
    
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if color[i] != -1:
                continue
            else:
                color[i] = 1 - color[v]
                queue.append(i)
    return color

n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    a,b = (int(x) for x in input().split())
    a -= 1; b -= 1
    g[a].append(b)
    g[b].append(a)
    
color = [-1 for _ in range(n)]
res = bfs(0)

ans = []
if res.count(1) > res.count(0):
    for i in range(n):
        if res[i] == 1:
            ans.append(i+1)
        if len(ans) == n // 2:
            print(*ans)
            exit()
else:
    for i in range(n):
        if res[i] == 0:
            ans.append(i+1)
        if len(ans) == n // 2:
            print(*ans)
            exit()