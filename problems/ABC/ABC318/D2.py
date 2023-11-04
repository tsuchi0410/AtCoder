from collections import deque

INF = 10**18
N = int(input())
D = [0] * (N - 1)
for i in range(N - 1):
    D[i] = [0] * (i + 1) + list(map(int, input().split()))

G = [[] for _ in range(N)]
for i in range(N):
	for j in range(N):
		if i == j:
			continue
		G[i].append(j)

def dfs(pos, G, visited, f, cnt, ans):
	ans = max(ans, cnt)
	print(ans)
	visited[pos] = True
	for i in G[pos]:
		if visited[i] == False:
			if f == True:
				if pos > i:
					cnt += D[i][pos]
				else:
					cnt += D[pos][i]
				f = False
			else:
				f = True
			dfs(i, G, visited, f, cnt, ans)
	

for i in range(N):
	visited = [False] * N
	f = True
	cnt = 0
	ans = 0
	dfs(i, G, visited, f, cnt, ans)
