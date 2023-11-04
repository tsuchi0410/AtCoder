N,M,X = (int(x) for x in input().split())
G = [[] for _ in range(N)]

for i in range(M):
    
    A,B = (int(x) for x in input().split())
    G[A].append(B)
    G[B].append(A)
    
l = set()
for i in range(len(G[X])):
    
    a = G[X][i]
    for j in range(len(G[a])):
        
        if G[a][j] != X and G[a][j] not in G[X]:
            l.add(G[a][j])
        
print(len(l))