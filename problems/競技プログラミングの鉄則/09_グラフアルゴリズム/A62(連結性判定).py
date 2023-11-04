import sys
sys.setrecursionlimit(10 ** 8)

def dfs(pos, G, visited):
	visited[pos] = True
	for i in G[pos]:
		if visited[i] == False:
			dfs(i, G, visited)

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
dfs(0, G, visited)

# 連結性判定 : すべて訪れた -> 連結
print("No") if False in visited else print("Yes") 