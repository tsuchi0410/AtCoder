class unionfind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n # 要素 x の親頂点の番号 (自身が根の場合は −1)
        self.rank = [0] * n # 要素 x の属する根付き木の高さ
        self.siz = [1] * n # 要素 x の属する根付き木に含まれる頂点数

    # 根を求める
    def root(self, x):
        if self.par[x] == -1: return x # x が根の場合は x を返す
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
        # union by rank
        if self.rank[rx] < self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]
    
    # 連結成分個数カウント
    def CountConnectedComponent(self, N):
        res = 0
        for i in range(N):
            if uf.root(i) == i: # 根の個数を数える
                res += 1
        return res

n, m = (int(x) for x in input().split())

uf = unionfind(n)
for i in range(m):
    
    a, b = (int(x) for x in input().split())
    uf.unite(a, b)

ans = uf.CountConnectedComponent(n)
print(ans)