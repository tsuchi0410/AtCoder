"""
・概要
単一始点最短経路問題(SSSP)を解くアルゴリズム。
辺のコストに負が含まれていても正しく動き、負閉路も検出することができる。

・計算量
O(|E||V|)
"""
INF = 10**18

def bellman_ford(start):

    # dist = [i][j] : i 回目のステップ終了時の距離
    dist = [[INF for _ in range(N)] for _ in range(2 * N)]
    # スタート地点
    dist[0][start] = 0

    # 1 回目の探索
    for i in range(1, N):
        # 前のステップのコストを初期値とする
        for j in range(N):
            dist[i][j] = dist[i - 1][j]
        
        for v, now in enumerate(G):
            for next_v, next_cost in now:
                if dist[i][v] != INF:
                    tmp = dist[i][v] + next_cost
                    if tmp < dist[i][next_v]:
                        dist[i][next_v] = tmp
    
    # 最後に更新があった頂点をマーク
    for v in range(N):
        if dist[N - 2][v] != dist[N - 1][v]:
            dist[N - 1][v] = -INF
    
    # 2 回目の探索
    # 負閉路に含まれる頂点から頂点 N − 1 にたどり着くことができるか
    for i in range(N, 2 * N):
        # 前のステップのコストを初期値とする
        for j in range(N):
            dist[i][j] = dist[i - 1][j]

        for v, now in enumerate(G):
            for next_v, next_cost in now:
                if dist[i][v] == -INF:
                    dist[i][next_v] = -INF

    return dist
    
    
# N : 頂点数, M : 辺数
N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    a, b, w = map(int, input().split())
    
    # 有向グラフ
    G[a].append((b, w))

dist = bellman_ford(0)

# dist[i][j] == INF : 到達不可能
# dist[i][j] == -INF : 負経路を経由して到達可
# else : 到達可能(最短経路)
