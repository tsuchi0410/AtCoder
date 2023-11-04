from collections import deque
from collections import defaultdict, Counter

# 辺情報を表す構造体
class edge:
    def __init__(self, start, end, leng):
        self.start = start  # 辺の始点
        self.end = end      # 辺の終点
        self.leng = leng    # 辺の重み
    
    # 構造体 edge の比較関数
    def __lt__(self, other):
        return self.leng < other.leng

# Union-Find
class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        for i in range(n):
            self.par[i] = i
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == x: return x # x が根の場合は x を返す
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False # すでに同じグループのときは何もしない
        # union by size
        if self.siz[rx] > self.siz[ry]: # ry 側の siz が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]

        

def is_ok(mid, X, Y):
    # 条件を満たすかどうか？問題ごとに定義
    cnt = 0
    for a, b in L: 
        D = ((X - a) ** 2 + (Y - b) ** 2) ** 0.5
        if D <= mid:
            cnt += 1
    return cnt

def meguru_bisect(ng, ok, X, Y):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    now = 0
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, X, Y) > now:
            ok = mid
        else:
            ng = mid
    return ok


N, M, K = map(int, input().split())
x = []
y = []
for _ in range(N):
    xx, yy = map(int,input().split())
    x.append(xx)
    y.append(yy)
graph_edges = [[] for _ in range(M)]    # graph_edges[i]：i 番目の辺情報
d = {}
for i in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph_edges[i] = edge(u, v, w)
    d[(u, v)] = 0
L = []
for _ in range(K):
    a, b = map(int,input().split())
    L.append([a, b])

# 辺情報を重みの昇順にソートする
graph_edges.sort()
# 要素数 N の Union-Find を用意する
uf = UnionFind(N)

ans = 0 # 答えとなる変数
P = [0] * N
B = []
for i in range(M):
    # 重みが i 番目に小さい辺は、頂点 u, v を結ぶ、重み w の辺であるとする
    u, v, w = graph_edges[i].start, graph_edges[i].end, graph_edges[i].leng

    # 頂点 u, v がすでに同じグループに属するなら、この辺は採用しない
    if uf.issame(u, v): continue
    # そうでないなら、この辺を採用する
    # Union-Find 上で u, v を統合して、答えに w を足す

    # 採用
    uf.unite(u, v)
    d[(u, v)] = 1

for i in range(N):
    res = meguru_bisect(0, 5000, x[i], y[i])
        



for i in d.values():
    B.append(i)

print(*P, sep = " ")    
print(*B, sep = " ")