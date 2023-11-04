from collections import deque

def bfs(start):
    
    q = deque([start])
    depth = [-1] * N # 頂点数
    depth[start] = 0
    
    while q:
        v = q.popleft()
        
        for next in G[v]:
            if depth[next] == -1:
                depth[next] = depth[v] + 1
                q.append(next)
        
    return depth