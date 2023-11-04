#N = int(input())
#L = list(map(int,input().split()))

N, M = (int(x) for x in input().split())

g = []
for i in range(N):
    g.append([0]*N)

U = []
V = []
for i in range(M):
    x, y = (int(x) for x in input().split())
    U.append(x)
    V.append(y)

for i in range(M):
    g[U[i]-1][V[i]-1] = 1
    g[V[i]-1][U[i]-1] = 1

l = []
c = 0
for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            for k in range(N):
                if g[j][k] == 1:
                    if g[i][k] == 1:
                        c += 1
                        
print(int(c/6))