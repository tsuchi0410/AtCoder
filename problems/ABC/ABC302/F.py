import heapq
from collections import defaultdict
INF = 10**18

# N : 集合の数, M : 整数の数
N, M = map(int, input().split())

# 整数の総数は、2 <= M <= 2 * 10 ^ 5 なので、愚直に整数同士で辺を貼ると O(N^2) で TLE する
# そこで、超頂点を導入する。
# 集合の数の分だけ超頂点を追加する
# 数同士で辺を貼るのではなく、数と超頂点（集合）で辺を貼ることにより、O(N + M) になる
G = [[] for _ in range(N + M)]

dic = defaultdict(list)
for i in range(N):
    A = int(input())
    S = list(map(int,input().split()))
    # 数と集合の関係を管理
    # key -> val = 数字 -> 集合
    for j in S:
        dic[j - 1].append(i)

for v, e in dic.items():
    for i in range(len(e)):
        G[v].append((e[i] + M, 1))
        G[e[i] + M].append((v, 1))

# ダイクストラ法で頂点 0 から各頂点までの最短経路長を求める。
# heapq を用意
# コストの小さい順に取り出すので、(cost, v)
hq = []
hq.append((0, 0))
heapq.heapify(hq)

# 距離
dist = [INF] * (N + M)
# スタート地点
dist[0] = 0

# 確定している頂点かを管理
seen = [False] * (N + M)

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

if dist[M - 1] == INF:
    print(-1)
else:
    # 別の集合へ移動するとき超頂点を必ず経由するので、距離は半分
    print(dist[M - 1] // 2 - 1)