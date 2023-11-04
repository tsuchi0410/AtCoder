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

H, W = map(int, input().split())
S = [input() for _ in range(H)]

# ２次元配列を１次元配列化
def flatten(h, w):
    return h + H * w

G = {}
for i in range(H):
    for j in range(W):
        G[(i, j)] = flatten(i, j)

uf_h = UnionFind(H * W)
uf_w = UnionFind(H * W)
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue
        for i, j in [[h - 1, w], [h, w + 1]]:
            if not 0 <= i < H:
                continue
            if not 0 <= j < W:
                continue

            if S[i][j] == ".":
                if i == h - 1:
                    uf_h.unite(G[(h, w)], G[(i, j)])
                else:
                    uf_w.unite(G[(h, w)], G[(i, j)])

ans = [0] * (H * W)
for l in uf_h.groups():
    for i in l:
        ans[i] += len(l)
for l in uf_w.groups():
    for i in l:
        ans[i] += len(l)

print(max(ans) - 1)