from collections import deque

def bfs(start):
    
    q = deque([start])
    seen = [False] * N # 頂点数
    
    while q:
        v = q.popleft()
        seen[v] = True
        
        for next in G[v]:
            if seen[next] == True:
                continue
            
            # 処理
            
            
            q.append(next)
    
    return 