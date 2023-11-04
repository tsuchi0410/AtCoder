import sys
sys.setrecursionlimit(10 ** 8)
from collections import defaultdict

def dfs(pos, G, visited):
    visited[pos] = True

    if not C[pos] in color:
         ans.append(pos + 1)
    color[C[pos]] += 1 
    
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)

    color[C[pos]] -= 1
    if color[C[pos]] == 0:
        del color[C[pos]]

N = int(input())
C = list(map(int,input().split()))
G = [[] for _ in range(N)]
for _ in range(N - 1):
	a, b = map(int,input().split())
	a -= 1
	b -= 1
	G[a].append(b)
	G[b].append(a)

ans = []
visited = [False] * (N)
color = defaultdict(int)
dfs(0, G, visited)
ans.sort()
print(*ans, sep = "\n")