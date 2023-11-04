from collections import defaultdict

class UnionFind():
    """
    Union Find木クラス

    Attributes
    --------------------
    n : int
        要素数
    patents : list
        指定した要素の親（1つ上の）要素を格納
        指定した要素が根の場合は，
        -(グループの要素数)  を格納
        => sizeメソッドに反映
    """
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """
        ノードxの根を見つける
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """
        木に新たな要素を併合（マージ）

        Parameters
        ---------------------
        x, y : int
            併合するノード
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """
        xの属する木のサイズ
        """
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """
        x, yが同じ木に属するか判定
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """
        
        """        
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """
        全ての根をリストで返す
        """ 
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """
        グループの数を返す
        """ 
        return len(self.roots())

    def all_group_members(self):
        """
        全てのグループの要素情報を辞書で返す
        """         
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        """
        print(uf)で全てのグループの要素情報を簡単に出力する
        """ 
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
    
    def members(self, x):
        r = self.root(x)
        return [i for i in range(self.n) if self.root(i) == r]

N, M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int,input().split())
    A -= 1
    B -= 1
    # 小さい方から大きい方のみに辺を貼る
    G[A].append(B)

uf = UnionFind(N)
ans = [0]
cnt = 0
for v in range(N - 1, 0, -1):
    # 頂点を追加
    cnt += 1
    for w in G[v]:
        if uf.find(v) != uf.find(w):
            cnt -= 1
        uf.union(v, w)
    ans.append(cnt)
ans.reverse()
print(*ans, sep = "\n")