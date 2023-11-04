from collections import deque

def bfs(start):
    
    q = deque([start])
    d = [-1] * N
    d[start] = 0
    ans = [-1] * N
    ans[0] = 0
    
    while q:
        v = q.popleft()
        
        for next in G[v]:
            if d[next] == -1:
                # 処理
                ans[next] = v
                d[next] = d[v] + 1
                q.append(next)
    
    return ans

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

ans = bfs(0)
for i in range(N):
    if ans[i] == -1:
        print("No")
        exit()
    ans[i] += 1

print("Yes")
print(*ans[1:], sep="\n")    