N = int(input())
G = [[] for _ in range(N)]
A = list(map(int, input().split()))
for i in range(N):
    A[i] -= 1
    G[i].append(A[i])

goal = 10 ** 18
seen = [False] * N
for i in range(N):
    if seen[i] == False:
        now = i
        seen[i] = True
        while True:
            nv = G[now][0]
            if seen[nv] == True:
                goal = nv
                break
            elif seen[nv] == False:
                seen[nv] = True
                now = nv
    
    if goal != 10 ** 18:
        break

now = goal
ans = [now]
while True: 
    nv = G[now][0]
    if nv == goal:
        for i in range(len(ans)):
            ans[i] += 1
        print(len(ans))
        print(*ans)
        exit()
    else:
        ans.append(nv)
        now = nv