from collections import deque

def bfs(X, Y, P):
    
    q = deque([[X, Y, P]])
    ans.add(P)
    
    while q:
        x, y, p = q.popleft()
        
        
        for xx, yy, pp in L: 
            if not pp in ans:
                d = ((x - xx) ** 2 + (y - yy) ** 2) ** 0.5
                if d <= D:
                    ans.add(pp)
                    q.append([xx, yy, pp])

N, D = map(int,input().split())
L = []
for _ in range(N):
    x, y = map(int,input().split())
    L.append([x, y, _])

ans = set()
bfs(L[0][0], L[0][1], L[0][2])

for i in range(N):
    if i in ans:
        print("Yes")
    else:
        print("No")