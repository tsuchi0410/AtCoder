"""
・概要
単一始点最短経路問題(SSSP)を解くアルゴリズム。 
頂点 0 から各頂点までの最短経路長を求める。
到達するまでのコストが小さい方からコストを伝搬させていく。

・計算量
O((|E|+|V|)log|V|)
"""

import heapq
INF = 10**18

def dijkstra(start):
    
    # heapq を用意
    # コストの小さい順に取り出すので、(cost, v)
    hq = [(0, start)]
    heapq.heapify(hq)
    
    # 距離
    dist = [INF] * N
    # スタート地点
    dist[start] = 0
    
    # 確定している頂点かを管理
    seen = [False] * N
    
    while hq:
        cost_v, v = heapq.heappop(hq)
        
        # hq の最小要素が確定しているか確認
        if seen[v] == True:
            continue

        seen[v] = True
        for u, cost_u in G[v]:
            if dist[u] > cost_v + cost_u:
                dist[u] = cost_v + cost_u
                heapq.heappush(hq, (dist[u], u))
    
    return dist

# N : 頂点数, M : 辺数
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, w = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append((b, w))
    G[b].append((a, w))

dist = dijkstra(0)

print(dist)