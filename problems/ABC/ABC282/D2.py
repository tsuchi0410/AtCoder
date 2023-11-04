class UnionFind:
    """
    0-indexed
    """

    from typing import List

    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n

    def unite(self, x, y) -> int:
        """
        xとyを併合
        """

        x = self.root(x)
        y = self.root(y)

        if x == y:
            return 0

        if self.parent[x] > self.parent[y]:
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x

        return self.parent[x]

    def is_same(self, x, y) -> bool:
        """
        xとyが同じ連結成分か判定
        """
        return self.root(x) == self.root(y)

    def root(self, x) -> int:
        """
        xの根を取得
        """
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def size(self, x) -> int:
        """
        xが属する連結成分のサイズを取得
        """
        return -self.parent[self.root(x)]

    def all_sizes(self) -> List[int]:
        """
        全連結成分のサイズのリストを取得
        計算量: O(N)
        """
        sizes = []

        for i in range(self.n):
            size = self.parent[i]
            if size < 0:
                sizes.append(-size)
        return sizes

    def groups(self) -> List[List[int]]:
        """
        全連結成分のサイズの内容のリストを取得
        計算量: O(N・α(N))
        なんでACLはO(N)でできるんでしょうね
        """
        groups = dict()

        for i in range(self.n):
            p = self.root(i)
            if not groups.get(p):
                groups[p] = []
            groups[p].append(i)

        return list(groups.values())


from collections import deque

n,m=(int(x) for x in input().split())
g=[[] for _ in range(n)]
uf=UnionFind(n)
for i in range(m):
    u,v=(int(x) for x in input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
    uf.unite(u-1,v-1)

if len(uf.groups()) >= 3:
    print(0)
    exit()
elif len(uf.groups()) == 2:
    l = []
    for group in uf.groups():
        l.append(len(group))
    m = l[0] * l[1]

num = 0
loop = 0
for group in uf.groups():
    color = [-1 for _ in range(n)]    # color[v]：頂点 v の色が黒なら 1, 白なら 0, 未探索なら -1
    ans = 'Yes'
    # 全ての頂点について
    for v in group:
        # 頂点 v がすでに訪問済みであれば、スキップ
        if color[v] != -1: continue
        # そうでなければ、頂点 v を含む連結成分は未探索
        # 頂点 v の色を白で決め打ちしたうえで、幅優先探索を行う
        deq = deque([]) # 探索候補の頂点番号を入れるキュー
        color[v] = 0
        deq.append(v)
        # キューに要素が残っている限り
        while len(deq) > 0:
            qv = deq.popleft()
            # 頂点 qv に隣接している頂点 nv について、
            for nv in g[qv]:
                # nv がすでに探索済みならば、スキップする
                if color[nv] != -1:
                    # 隣り合う頂点どうしが同じ色なら、答えは No
                    if color[nv] == color[qv]: ans = 'No'
                    continue
                
                # そうでなければ、頂点 nv の色を color[qv] と逆にしたうえで、nv も探索候補に入れる
                color[nv] = 1 - color[qv]
                deq.append(nv)
    
    if ans == 'No':
        print(0)
        exit()
    else:
        c0 = 0
        c1 = 0
        # 各グラフの色の数
        for v in group:
            if color[v] == 0:
                c0 += 1
            else:
                c1 += 1
        # つながってる部分除外
        for v in group:
            me = color[v]
            cnt0 = 0
            cnt1 = 0
            for u in g[v]:
                if color[u] == 0:
                    cnt0 += 1
                else:
                    cnt1 += 1
            if me == 0:
                num += c1 - cnt1
            else:
                num += c0 - cnt0

if len(uf.groups()) == 1:
    print(num//2)
else:
    print(num//2 + m)
