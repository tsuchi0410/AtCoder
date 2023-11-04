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
    
# ２次元配列を１次元配列化
def flatten(r, c):
    return r+h*c

h, w = (int(x) for x in input().split())
q = int(input())
g = [[False] * w for _ in range(h)]
uf = UnionFind(h * w)
for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        r, c = query[1], query[2]
        r -= 1; c -= 1
        g[r][c] = True
        node = flatten(r, c)
        for y, x in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
            if y < 0 or x < 0:
                continue
            if y >= h or x >= w:
                continue
            if g[y][x] == True:
                node2 = flatten(y, x)
                uf.unite(node, node2)
        
    else:
        ra, ca, rb, cb = query[1], query[2], query[3], query[4]
        ra -= 1; ca -= 1; rb -= 1; cb -= 1
        if g[ra][ca] == True and g[rb][cb] == True:
            node = flatten(ra, ca)
            node2 = flatten(rb, cb)
            ans = uf.is_same(node, node2)
            if ans == True:
                print('Yes')
            else:
                print('No')
        else:
            print('No')