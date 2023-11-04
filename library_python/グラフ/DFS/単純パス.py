"""
Pythonで提出
"""

# 頂点0 -> N-1 への単純パス

import sys
sys.setrecursionlimit(10 ** 8)

def dfs(pos, G, visited):
    path.append(pos + 1)
    visited[pos] = True
	
    if pos == N - 1:
        print(*path)
        exit()

    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)
    path.pop()

# N:頂点数, M:辺数
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
	a, b = map(int,input().split())
	a -= 1
	b -= 1
	G[a].append(b)
	G[b].append(a)

visited = [False] * (N)
path = []
dfs(0, G, visited)


