N, M = (int(x) for x in input().split())

G = [[] for _ in range(N)]
for i in range(M):
    A, B = (int(x) for x in input().split())
    
    G[A].append(B)
    G[B].append(A)

a = -1
idx = 0
for i in range(N):
    if a < len(G[i]):
        a = len(G[i])
        idx = i

print(*sorted(G[idx]))