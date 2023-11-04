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
for i in range(M):
    u, v = map(int,input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

dist = []
for i in range(N):
    dist.append(bfs(i))

ans = [1] * N
K = int(input())
op = []
for i in range(K):
    p, d = map(int,input().split())
    p -= 1
    op.append([p, d])
    for j in range(N):
        if dist[p][j] < d:
            ans[j] = 0

for i in range(K):
    f = False
    p, d = op[i]
    for j in range(N):
        if dist[p][j] == d and ans[j] == 1:
            f = True
            break
    if f == False:
        print("No")
        exit()

print("Yes")
print(*ans, sep = "")
    