INF = 10**18

def warshall_floyd():

    ans = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if cost[i][k] != INF and cost[k][j] != INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
        
        for i in range(N):
            for j in range(N):
                if cost[i][j] != INF:
                    ans += cost[i][j]


    return ans
    
# N : 頂点数, M : 辺数
N, M = map(int, input().split())

# cost[i][j] : 頂点 v_i から 頂点 v_j へ到達するための辺コストの和
cost = [[INF] * N for _ in range(N)]

for _ in range(M):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    
    # 有向グラフ
    cost[a][b] = w

for i in range(N):
    cost[i][i] = 0

ans = warshall_floyd()
print(ans)