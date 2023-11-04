from collections import deque

def bfs(start):
    
    q = deque([start])
    depth = [-1] * N # 頂点数
    depth[start] = 0
    
    while q:
        v = q.popleft()
        
        for next in G[v]: # G:グラフ
            if depth[next] == -1:
                depth[next] = depth[v] + 1
                q.append(next)
        
    return depth

N, M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

for v in range(N):
    print(bfs(i))