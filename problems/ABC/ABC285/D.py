from collections import defaultdict, deque
N = int(input())
d = {}
s = []
t = []
for i in range(N):
    a, b = ((x) for x in input().split())
    s.append(a)
    t.append(b)

cnt = 0
for i in range(N):
    if s[i] not in d:
        d[s[i]] = cnt
        cnt += 1

for i in range(N):
    if t[i] not in d:
        d[t[i]] = cnt
        cnt += 1

G = [[] for _ in range(len(d))]  # グラフを表現する隣接リスト (終点のインデックスから、始点の番号を取り出す)
deg = [0 for _ in range(len(d))] # deg[v]：頂点 v の出次数
for i in range(N):
    G[d[t[i]]].append(d[s[i]])
    # 頂点 a の出次数を 1 増やす
    deg[d[s[i]]] += 1


que = deque([]) # 探索候補の頂点番号を入れるキュー
# 頂点 v = 0, 1, …, N-1 の順に
for v in range(len(d)):
    # 頂点 v の出次数が最初の時点で 0 ならば、キューに v を入れる
    if deg[v] == 0: que.append(v)

order = []  # トポロジカルソート順を格納するための配列

# キューに要素が残っている限り
while len(que) > 0:
    # キューの先頭要素 v を取り出し、配列 order に挿入する
    v = que.popleft()
    order.append(v)
    
    # 頂点 v に隣接している頂点 v2 について、
    for v2 in G[v]:
        # v2 の出次数を 1 減らして、もし出次数が 0 になったらキューに v2 を入れる
        deg[v2] -= 1
        if deg[v2] == 0: que.append(v2)

# 全ての頂点が order に含まれているかによって、答えを変える
if len(order) != len(d):
    # order の要素数が N でなければ、order に含まれていない頂点があるので Yes
    print('No')
else:
    # order の要素数が N であれば、すべての頂点が order に含まれているので No
    print('Yes')