INF = 10**18

def warshall_floyd():

    for k in range(10):
        for i in range(10):
            for j in range(10):
                if cost[i][k] != INF and cost[k][j] != INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    return cost

H, W = map(int,input().split())
C = [list(map(int,input().split())) for _ in range(10)]
A = [list(map(int,input().split())) for _ in range(H)]

# cost[i][j] : 頂点 v_i から 頂点 v_j へ到達するための辺コストの和
cost = [[INF] * 10 for _ in range(10)]

for i in range(10):
    for j in range(10):
        a, b, w = i, j, C[i][j]
        
        # 有向グラフ
        cost[a][b] = w

for i in range(10):
    cost[i][i] = 0

cost = warshall_floyd()

ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] != -1:
            ans += cost[A[i][j]][1]

print(ans)
