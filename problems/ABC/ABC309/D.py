from collections import deque

def bfs(G, N, start):
    
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

N1, N2, M = map(int, input().split())
G1 = [[] for _ in range(N1 + N2)]
G2 = [[] for _ in range(N1 + N2)]
for _ in range(M):
    a, b = map(int, input().split())
    if a <= N1:
        a -= 1
        b -= 1
        G1[a].append(b)
        G1[b].append(a)
    else:
        a -= 1
        b -= 1
        G2[a].append(b)
        G2[b].append(a)

d1 = bfs(G1, N1 + N2, 0)
d2 = bfs(G2, N1 + N2, N1 + N2 - 1)

print(max(d1) + max(d2) + 1)
