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
        elif seen[v] == False:
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

for i in dist:
    if i == INF:
        print(-1)
    else:
        print(i)