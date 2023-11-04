import heapq
INF = 10**18

N, M, K = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

# コストの小さい順に取り出すので、(cost, v)
hq = []
# 距離
HP = [-1] * N
for _ in range(K):
    p, h = map(int,input().split())
    p -= 1
    hq.append([-h, p])
    HP[p] = h
heapq.heapify(hq)

while hq:
    h, v = heapq.heappop(hq)
    h = -h
    
    # hq の最小要素が確定しているか確認
    if HP[v] != h:
        continue

    for u in G[v]:
        if HP[u] < h - 1:
            HP[u] = h - 1
            if h - 1 > 0:
                heapq.heappush(hq, [-(h - 1), u])

ans = 0
l = []
for i, v in enumerate(HP):
    if v != -1:
        ans += 1
        l.append(i + 1)
print(ans)
print(*l)