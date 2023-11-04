from collections import deque
MOD = 10**9 + 7

def bfs(start):
    
    q = deque([start])
    depth = [-1] * N # 頂点数
    depth[start] = 0
    cnt = [0] * N
    cnt[0] = 1
    
    while q:
        v = q.popleft()
        
        for next in G[v]: # G:グラフ
            if depth[next] == -1:
                depth[next] = depth[v] + 1
                q.append(next)
                cnt[next] = cnt[v]
            elif depth[next] == depth[v] + 1:
                cnt[next] += cnt[v]
                cnt[next] %= MOD
                
        
    return cnt

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

res = bfs(0)
print(res[N-1])