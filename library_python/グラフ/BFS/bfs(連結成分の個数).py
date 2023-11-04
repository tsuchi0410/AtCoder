from collections import deque

def bfs(start):
    
    q = deque([start])
    
    while q:
        v = q.popleft()
        seen[v] = True
        
        for next in G[v]:
            if seen[next] == True:
                continue
            q.append(next)
    
    return

N, M = map(int, input().split())
G = [[] for _ in range(N)]
seen = [False] * N # 頂点数
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

cnt = 0
for i in range(N):
    if seen[i] == False:
        bfs(i)
        cnt += 1
print(cnt)