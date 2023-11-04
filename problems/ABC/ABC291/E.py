from collections import deque


N, M = map(int, input().split())
G = [[] for _ in range(N)]  # グラフを表現する隣接リスト (終点のインデックスから、始点の番号を取り出す)
deg = [0 for _ in range(N)] # deg[v]：頂点 v の出次数
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    # 通常のグラフとは逆で、G[b] に a を入れる
    G[b].append(a)
    # 頂点 a の出次数を 1 増やす
    deg[a] += 1

# 問題文の指示より、隣接リストの中身をソートしておく
for i in range(N):
    G[i].sort()

que = deque([]) # 探索候補の頂点番号を入れるキュー
# 頂点 v = 0, 1, …, N-1 の順に
for v in range(N):
    # 頂点 v の出次数が最初の時点で 0 ならば、キューに v を入れる
    if deg[v] == 0: que.append(v)

order = []  # トポロジカルソート順を格納するための配列

# キューに要素が残っている限り
while len(que) > 0:
    if len(que) > 1:
        print("No")
        exit()

    # キューの先頭要素 v を取り出し、配列 order に挿入する
    v = que.popleft()
    order.append(v)
    
    # 頂点 v に隣接している頂点 v2 について、
    for v2 in G[v]:
        # v2 の出次数を 1 減らして、もし出次数が 0 になったらキューに v2 を入れる
        deg[v2] -= 1
        if deg[v2] == 0: que.append(v2)

# 配列 order を反転させる
order.reverse()

ans = []
for i in range(N):
    ans.append([i, order[i]])

ans = sorted(ans,key=lambda x: x[1])

l = []
for i in range(N):
    l.append(ans[i][0] + 1)

print("Yes")
print(*l, sep = " ")