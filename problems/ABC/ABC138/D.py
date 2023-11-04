from collections import deque

def bfs(u):
    
    q = deque([u])
    seen = [False] * N
    
    while q:
        v = q.popleft()
        seen[v] = True
        
        for next in G[v]:
            if seen[next] == True:
                continue
            counter[next] += counter[v]
            q.append(next)
    
    return 
    

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
add = [list(map(int, input().split())) for _ in range(Q)]

counter = [0] * N
for p, x in add:
    counter[p-1] += x

bfs(0)

print(*counter)