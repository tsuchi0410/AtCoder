import heapq
INF = 10**18

N, M, X, Y = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, t, k = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append((b, t, k))
    G[b].append((a, t, k))

X -= 1
# heapq を用意
# コストの小さい順に取り出すので、(cost, v)
hq = [(0, X)]
heapq.heapify(hq)

# 距離
dist = [INF] * N
# スタート地点
dist[X] = 0

# 確定している頂点かを管理
seen = [False] * N

while hq:
    cost_v, v = heapq.heappop(hq)
    
    # hq の最小要素が確定しているか確認
    if seen[v] == True:
        continue

    seen[v] = True
    for u, cost_u, ku in G[v]:
        if v == X:
            waiting = 0
        else:
            if dist[v] <= ku:
                waiting = ku - dist[v]
            else:
                if dist[v] % ku == 0:
                    waiting = 0
                else:
                    x = dist[v] // ku + 1
                    waiting = ku * x - dist[v]

        if dist[u] > cost_v + cost_u + waiting:
            dist[u] = cost_v + cost_u + waiting
            heapq.heappush(hq, (dist[u], u))
    

ans = dist[Y - 1]
if ans == INF:
    print(-1)
else:
    print(ans)