# O(N)

from collections import deque

# 入力の受け取り
N, M = (int(x) for x in input().split())
G = [[] for _ in range(N)]    # グラフを表現する隣接リスト
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

r = 0   # 適当な頂点 r をとる (この値は 0 以上 N-1 以下であれば、何でもよい)
# 頂点 r を始点として幅優先探索を行う
dist_r = [-1 for _ in range(N)]   # dist_r[i]：頂点 r から頂点 i までの距離
que = deque([]) # これから調べるべき頂点を管理するキュー
# 頂点 r を始点として登録する
dist_r[r] = 0
que.append(r)

# キューが空になるまで、探索を続ける
while len(que) > 0:
    # 次に調べるべき頂点を v とする
    v = que.popleft()

    # 頂点 v に隣接する頂点 nv について、
    for nv in G[v]:
        # 頂点 nv が探索済みならば、スキップする
        if dist_r[nv] != -1: continue
        # そうでないならば、dist_r[nv] を確定させてキューに nv を挿入する
        dist_r[nv] = dist_r[v] + 1
        que.append(nv)

# 頂点 r から最も遠い頂点番号を s とおく
s = dist_r.index(max(dist_r))
dist_s = [-1 for _ in range(N)]   # dist_s[i]：頂点 s から頂点 i までの距離

# 頂点 s を始点として登録する
dist_s[s] = 0
que.append(s)

# キューが空になるまで、探索を続ける
while len(que) > 0:
    # 次に調べるべき頂点を v とする
    v = que.popleft()

    # 頂点 v に隣接する頂点 nv について、
    for nv in G[v]:
        # 頂点 nv が探索済みならば、スキップする
        if dist_s[nv] != -1: continue
        # そうでないならば、dist_r[nv] を確定させてキューに nv を挿入する
        dist_s[nv] = dist_s[v] + 1
        que.append(nv)

print(dist_s)