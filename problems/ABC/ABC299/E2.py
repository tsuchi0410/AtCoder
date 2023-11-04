from collections import deque

def bfs(start):
    q = deque(start)
    ans = [-1] * N # 頂点数
    for i in range(len(start)):
        ans[start[i][0]] = 0
    
    while q:
        v, d = q.popleft()
        
        for next in G[v]: # G:グラフ
            if ans[next] == -1 and d > 0:
                ans[next] = 0
                q.append([next, d - 1])
            elif ans[next] == -1 and d == 0:
                ans[v] = 1
            elif ans[v] == 1 and d == 0:
                print("No")
                exit() 
        print(ans)
        
    return ans

N, M = map(int,input().split())
G = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int,input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

K = int(input())
op = []
for _ in range(K):
    p, d = map(int,input().split())
    op.append([p - 1, d])
ans = bfs(op)
print(ans)
