N, M = (int(x) for x in input().split())

G = [[] for i in range(N)]
for i in range(M):
    A, B = (int(x) for x in input().split())
    
    G[A].append(B)
    
for i in range(N):
    print(*sorted(G[i]), sep = ' ')