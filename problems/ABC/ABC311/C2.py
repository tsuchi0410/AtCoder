"""
dfs : 有向辺のサイクル検出
ある頂点において、行きがけ順は true だが帰りがけ順が false であるとき、サイクルと判定
復元は、サイクル判定がされたらその頂点を記録しそこから戻る
"""

import sys
sys.setrecursionlimit(10 ** 8)

def dfs(G, v):
    seen[v] = True  # 行きがけ時に true
    history.append(v)
    for u in G[v]:
        if finished[u]:
            continue
        if seen[u] == True and finished[u] == False:  # サイクル検出
            global pos
            pos = u
            return True
        if dfs(G, u):
            return True 
    finished[v] = True  # 帰りがけ時に true
    history.pop()
    return False


N = int(input())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for i in range(N):
    G[i].append(A[i] - 1)

seen = [False] * N
finished = [False] * N
for i in range(N):
    history = []
    pos = -1
    if seen[i] == False:
        dfs(G, i)
        if len(history) != 0:
            start = history.index(pos)
            ans = history[start:]
            for i in range(len(ans)):
                ans[i] += 1
            print(len(ans))
            print(*ans)
            exit()