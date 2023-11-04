# 入力
N, M = map(int, input().split())
G = [[] for i in range(N)]

for i in range(M):
    A, B = map(int, input().split())

    # 頂点 A から頂点 B への辺を張る
    G[A].append(B)

    # 無向グラフの場合は次も実施
    # G[B].append(A)