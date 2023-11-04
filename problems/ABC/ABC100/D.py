N, M = map(int, input().split())
A = []
L = []
for _ in range(N):
    x, y, z = map(int, input().split())
    A.append(x)
    A.append(y)
    A.append(z)
    L.append([x, y, z])

# 集合型にすることで重複を除去し、小さい順にソートする
B = sorted(set(A))
# B の各要素が何番目の要素なのかを辞書型で管理する
D = { v: i for i, v in enumerate(B) }
# 答え
# [1, 4, 3, 3, 3, 2, 0, 5]
list(map(lambda v: D[v], A)))