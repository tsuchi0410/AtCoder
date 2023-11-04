from collections import deque

N = int(input())
C = [0] * N
P = [0] * N
for i in range(N):
    c, *p = list(map(int, input().split()))
    C[i] = c
    P[i] = p
    for j in range(c):
        P[i][j] -= 1

# 探索する範囲
d = [-1] * (N)

# 始点
d[0] = 0
q = deque([0])

while q:
    v = q.popleft()
    
    # 次見る場所
    next = []
    for i in range(C[v]):
        next.append(P[v][i])

    # 有向辺を貼りながらBFS
    for u in next:
        if d[u] == -1:
            d[u] = d[v] + 1
            q.append(u)

def tp_sort(G, deg):
    # 入ってくる有向辺を持たないノードを列挙
    q = deque()
    for v in range(N):  # N : 頂点数
        if deg[v] == 0:
            q.append(v)

    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for u in G[v]:
            deg[u] -= 1
            if deg[u] == 0:  # 入次数が 0 になったら q に追加
                q.append(u)

    return ans

G = [[] for _ in range(N)]
deg = [0] * N
for i in range(N):
    for j in range(C[i]):
        G[i].append(P[i][j])
        deg[P[i][j]] += 1

lst = (tp_sort(G, deg))
# for i in range(len(lst)):
#     lst[i] += 1
lst.reverse()

ans = []
d[0] = -1
for i in range(N):
    if d[lst[i]] != -1:
        ans.append(lst[i] + 1)

print(*ans)