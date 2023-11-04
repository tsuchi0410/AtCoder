from collections import deque

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))

depth = [-1] * N # 頂点数
for i in G:
    if len(i) >= 1:
        for v, w in i:
            q = deque([(v, w)])
            depth[v] = 0
            break
    break

while q:
    v, w = q.popleft()
    for next_v, next_w in G[v]:
        if depth[next_v] == -1:
            if next_w % 2 == 0:
                depth[next_v] = depth[v]
            else:
                depth[next_v] = depth[v] ^ 1
            
            print(depth)
            q.append((next_v, next_w))
    

print(G)
print(*depth)