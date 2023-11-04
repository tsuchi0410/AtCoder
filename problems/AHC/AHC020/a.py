



N, M, K = map(int,input().split())
x = []
y = []
for _ in range(N):
    xx, yy = map(int,input().split())
    x.append(xx)
    y.append(yy)
G = [[] for _ in range(N)]
w = []
for _ in range(M):
    u, v, ww = map(int,input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
    w.append(ww)
a = []
b = []
for _ in range(K):
    aa, bb = map(int,input().split())
    a.append(aa)
    b.append(bb)

visited = [False] * (N)
dfs(0, G, visited)
