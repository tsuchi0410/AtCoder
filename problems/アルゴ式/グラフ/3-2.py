from collections import deque

n, m = (int(x) for x in input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a,b = (int(x) for x in input().split())
    g[a].append(b)
    g[b].append(a)

def bfs(u):
    queue = deque([u])
    
    d = [None] * n
    d[u] = 0
    
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)

                
    return d

a = bfs(0)
print(max(a))



