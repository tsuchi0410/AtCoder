class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

#### segfunc ####
def segfunc(x, y):
    return min(x, y)
#################

INF = 10**18
##### 初期化 #####
ide_ele = INF
##################

N = int(input())
L = []
A = []
for _ in range(N):
    h, w, d = map(int, input().split())
    L.append([h, w, d])
    A.append(h)
    A.append(w)
    A.append(d)

# 座標圧縮
B = sorted(set(A))
D = {v: i for i, v in enumerate(B)}
A = list(map(lambda v: D[v], A))
idx = 0
for i in range(N):
    for j in range(3):
        L[i][j] = A[idx]
        idx += 1

# h <= w <= d
for i in range(N):
    L[i] = sorted(L[i])

# h について昇順、同じ h については w について降順
L.sort()
dic = {}
for h, w, d in L:
    if not h in dic:
        dic[h] = []
        dic[h].append([w, d])
    else:
        dic[h].append([w, d])

L = []
for h, v in dic.items():
    if len(v) >= 2:
        dic[h].sort(reverse=True)
        for w, d in v:
            L.append([h, w, d])
    else:
        for w, d in v:
            L.append([h, w, d])

a = [INF] * (len(B) + 10)
seg = SegTree(a, segfunc, ide_ele)
for h, w, d in L:
    if seg.query(0, w) < d:
        print("Yes")
        exit()
    if d < seg.query(w, w + 1):
        seg.update(w, d)

print("No")