# 座標圧縮 # NlogN
# 座標圧縮したい数列
A = [8, 100, 33, 33, 33, 12, 6, 1211]
# 集合型にすることで重複を除去し、小さい順にソートする
B = sorted(set(A))
# B の各要素が何番目の要素なのかを辞書型で管理する
D = { v: i for i, v in enumerate(B) }
# 答え
# [1, 4, 3, 3, 3, 2, 0, 5]
print(list(map(lambda v: D[v], A)))


# 2次元
X = []; Y = []
XX.sort(); YY.sort()
XD = { v : i + 1 for i, v in enumerate(sorted(set(XX))) }
YD = { v : i + 1 for i, v in enumerate(sorted(set(YY))) }
newX = list(map(lambda v: XD[v], X))
newY = list(map(lambda v: YD[v], Y))


# 文字列 -> 数値
N = int(input())
d = {}
a = []
cnt = 0
for i in range(N):
    b = input()
    if b not in d:
        d[b] = cnt
        cnt += 1
