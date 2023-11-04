N, M = map(int, input().split())
G = [[] for _ in range(N)]
deg = [0] * N
for _ in range(M):
    B, A = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)

ans = set()
for i in range(N):
    seen = [False] * N
    stack = [i]  # スタート
    while len(stack):
        v = stack.pop()
        if seen[v] == True:
            break
        seen[v] = True
        if len(G[v]) == 0:
            ans.add(v)
        for u in G[v]:
            stack.append(u)

if len(ans) == 1:
    ans = list(ans)
    print(ans[0] + 1)
else:
    print(-1)
