import heapq
INF = 10**18

def dijkstra(start):
    
    # heapq を用意
    # コストの小さい順に取り出すので、(cost, v)
    hq = [(0, start)]
    heapq.heapify(hq)
    
    # 距離
    dist = [INF] * (2 * N)
    # スタート地点
    dist[start] = 0
    
    # 確定している頂点かを管理
    seen = [False] * (2 * N)
    
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

N, M, K = map(int,input().split())
G = [[] for _ in range(2 * N)]
for _ in range(M):
    u, v, a = map(int,input().split())
    u -= 1
    v -= 1
    if a == 1:
        G[u].append((v, 1))
        G[v].append((u, 1))
    elif a == 0:
        G[u + N].append(((v + N), 1))
        G[v + N].append(((u + N), 1))
s = list(map(int,input().split()))
for v in s:
    v -= 1
    G[v].append(((v + N), 0))
    G[v + N].append((v, 0))

dist = dijkstra(0)

ans = min(dist[N - 1], dist[N - 1 + N])
print(-1) if ans == INF else print(ans)