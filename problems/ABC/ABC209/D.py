from collections import deque

def bfs(u):
    queue = deque([u])
    
    d = [None] * (n+1)
    d[u] = 0
    
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)

                
    return d

n, q = (int(x) for x in input().split())
g = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = (int(x) for x in input().split())
    # 有向グラフ
    g[a].append(b)
    # 無向グラフ
    g[b].append(a)

a = bfs(1)
for i in range(q):
    x, y = (int(x) for x in input().split())
    if (a[x] - a[y]) % 2 != 0:
        print('Road')
    else:
        print('Town')
