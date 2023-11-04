import heapq

# 辺情報を表す構造体
class edge:
    def __init__(self, end, leng):
        self.end = end      # 辺の終点
        self.leng = leng    # 辺の重み

INF = 10**9

n, m = map(int, input().split())
g = [[] for _ in range(n)] # G[i]：頂点 i を始点とする辺情報を格納する
for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(edge(v, w))
    g[v].append(edge(u, w))

def d(num):
    dist = [INF for _ in range(n)] # dist[i]：頂点 0 から頂点 i への暫定的な経路長
    dist[num] = 0
    done = [False for _ in range(n)]    # done[i]：頂点 i の最短距離が確定しているか

    hq = [] # (仮の最短距離、頂点番号) を管理するヒープ
    heapq.heapify(hq)

    # ヒープに最初の時点における情報を入れておく
    for v in range(n):
        heapq.heappush(hq, (dist[v], v))

    while len(hq) > 0:
        # ヒープの先頭要素を取り出す (v は頂点番号、d は 0 → v の仮の最短距離)
        [d, v] = heapq.heappop(hq)
        # 頂点 v の最短距離がすでに確定しているなら、何もしない
        if done[v]: continue

        # 頂点 v を始点とする辺 e について、更新を行う
        for e in g[v]:
            if dist[e.end] > dist[v] + e.leng:
                # 距離の更新がある場合には、ヒープに更新後の情報を入れる
                dist[e.end] = dist[v] + e.leng
                heapq.heappush(hq, (dist[e.end], e.end))
        # 頂点 v の最短距離を確定させる
        done[v] = True
    
    return dist

d1 = d(0)
d2 = d(n-1)

for i in range(n):
    print(abs(d1[0]-d1[i]) + abs(d2[i]-d2[n-1]))

