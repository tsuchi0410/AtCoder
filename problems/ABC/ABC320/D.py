from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    A, B, X, Y = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append([B, X, Y])
    G[B].append([A, -X, -Y])

q = deque([[0, 0, 0]])
seen = [False] * N # 頂点数
d = {}
d[0] = [0, 0]
while q:
    v, X, Y = q.popleft()
    seen[v] = True
    for next, NX, NY in G[v]:
        if seen[next] == True:
            continue
        d[next] = [d[v][0] + NX, d[v][1] + NY]
        q.append([next, NX, NY])

for i in range(N):
    if i in d:
        print(d[i][0], d[i][1])
    else:
        print("undecidable")