from collections import deque


def bfs(start, c):
    
    q = deque([start])
    seen = [False] * N # 頂点数
    l[start] = -1
    
    while q:
        v = q.popleft()
        seen[v] = True
        
        color = 1
        for next in G[v]:
            if seen[next] == True:
                continue
            if color == l[v]:
                color += 1
            l[next] = color
            ans[(v, next)] = l[next]
            q.append(next)
            c = max(c, color)
            color += 1
    
    return c


N = int(input())
G = [[] for _ in range(N)]
ans = {}
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
    ans[(a, b)] = 0

l = [1] * N
c = 0
c = bfs(0, c)
print(c)
for i in ans.values():
    print(i)