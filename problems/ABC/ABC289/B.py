from collections import deque

n, m = (int(x) for x in input().split())
a = list(map(int,input().split()))
g = [[] for _ in range(n)]
for i in range(m):
    x, y = a[i]-1, a[i]
    g[x].append(y)
    g[y].append(x)

def bfs(u):
    queue = deque([u])
    
    d = [None] * n
    d[u] = 0
    
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d

ans = []
idx = 0
while idx < n:
    res = bfs(idx)
    l = []
    for i in range(n):
        if res[i] != None:
            l.append(res[i] + idx + 1)
    l.reverse()
    for i in range(len(l)):
        ans.append(l[i])
    idx += len(l)

for i in range(len(ans)):
    ans[i] = str(ans[i])

print(" ".join(ans))