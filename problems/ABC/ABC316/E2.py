import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10 ** 8) 

def dfs(pos, G, visited):
	visited[pos] = True
	for i in G[pos]:
		if visited[i] == False:
			dfs(i, G, visited)
	path.append(pos)

N = int(input())
C = [0] * N
P = [0] * N
G = [[] for _ in range(N)]
for i in range(N):
	c, *p = map(int, input().split())
	C[i] = c
	P[i] = p
	for j in range(c):
		G[i].append(P[i][j] - 1)

path = []
visited = [False] * N
dfs(0, G, visited)
path.pop()
for i in range(len(path)):
	path[i] += 1
print(*path)