from collections import deque
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


N, M = map(int, input().split())
G = [[] for _ in range(N)]
deg = [0] * N
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    deg[B] += 1

lst = (tp_sort(G, deg))

dp = [0] * N
for v in lst:
    for u in G[v]:
        dp[u] = max(dp[u], dp[v] + 1)

print(max(dp))