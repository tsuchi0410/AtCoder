"""
ベルマンフォード法
・負の閉路があると正しく動かない場合がある。
・辺の重みが負でないならDijkstra法の方が高速。
・辺の情報についてのループをV-1回で全体の最短距離を求められる
・V回目のループで更新した場合はグラフに負の閉路がある
・計算量はO(VM)
"""
# ステップ数Kを求める

INF = float('inf')

n, m = map(int, input().split())
g = [[] for _ in range(m)]
for i in range(m):
    u, v, w = map(int, input().split())
    g[i] = [u, v, w]

dist = [INF for _ in range(n)]
dist[0] = 0
ans = -1
for k in range(n):
    flag = False
    
    for i in range(m):
        u, v, w = g[i]
        # distを更新する
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            flag = True
print(dist)