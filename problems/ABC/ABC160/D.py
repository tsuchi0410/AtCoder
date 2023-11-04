from collections import deque

def bfs(start):
    
    q = deque([start])
    d = [-1] * N
    d[start] = 0
    
    while q:
        v = q.popleft()
        
        for next in G[v]:
            if d[next] == -1:
                # 処理
                d[next] = d[v] + 1
                q.append(next)
        
    return d

N, X, Y = map(int, input().split())
X -= 1
Y -= 1
G = [[] for _ in range(N)]
for i in range(N-1):
    G[i+1].append(i)
    G[i].append(i+1)
G[X].append(Y)
G[Y].append(X)

ans = [0] * N
for i in range(N):
    l = bfs(i)
    for j in range(N):
        ans[l[j]] += 1

for i in range(N):
    ans[i] //= 2
print(*ans[1:], sep="\n")