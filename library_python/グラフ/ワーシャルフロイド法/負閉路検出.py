"""
・概要
全点対最短経路問題(APSP)を解くアルゴリズム。
グラフ G = (V, E) の全てのペア (v, w) 間の最短経路コストを求める。

・計算量
O(|V^3|)
"""
INF = 10**18

def warshall_floyd():

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if cost[i][k] != INF and cost[k][j] != INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    return 
    
# N : 頂点数, M : 辺数
N, M = map(int, input().split())

# cost[i][j] : 頂点 v_i から 頂点 v_j へ到達するための辺コストの和
cost = [[INF] * N for _ in range(N)]

for _ in range(M):
    a, b, w = map(int, input().split())
    
    # 有向グラフ
    cost[a][b] = w

for i in range(N):
    cost[i][i] = 0

warshall_floyd()

# 負閉路の検出
for i in range(N):
    if cost[i][i] < 0:
        print("NEGATIVE CYCLE")
        exit()
