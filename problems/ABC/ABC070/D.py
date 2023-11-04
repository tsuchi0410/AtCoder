import heapq
INF = 10**18

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append((b, c))
    G[b].append((a, c))
Q, K = map(int,input().split())
K -= 1

hq = [(0, K)]
heapq.heapify(hq)

# 距離
dist = [INF] * N
# スタート地点
dist[K] = 0

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

for _ in range(Q):
    x, y = map(int,input().split())
    x -= 1
    y -= 1
    print(dist[x] + dist[y])




