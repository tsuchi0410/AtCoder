from collections import deque

n, m = (int(x) for x in input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a,b = (int(x) for x in input().split())
    g[a].append(b)
    g[b].append(a)

def bfs(u):
    queue = deque([u])
    
    # uからの距離の初期化
    d = [None] * n
    # 自分(0)からの距離は0 
    d[u] = 0
    
    nodes = [[] for _ in range(n)]
    nodes[0] = [0]
    
    # queueが空になるまで探索
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
                nodes[d[i]].append(i)
                
    return d, nodes
    
# 0からの各点の距離
d, nodes = bfs(0)

for i in range(n):
    nodes[i].sort()
    print(*nodes[i])



