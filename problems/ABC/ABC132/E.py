from collections import deque
N, M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int,input().split())
    u -= 1
    v -= 1
    G[u].append(v)
S, T = map(int,input().split())
S -= 1
T -= 1
q = deque([[S, 0]])
depth = [[-1] * 3 for _ in range(N)]
depth[S][0] = 0
while q:
    v, f = q.popleft()
    for next in G[v]:
        if depth[next][(f + 1) % 3] == -1:
            depth[next][(f + 1) % 3] = depth[v][f] + 1
            q.append([next, (f + 1) % 3])
    if depth[T][0] != -1:
        print(depth[T][0] // 3)
        exit()
print(-1)