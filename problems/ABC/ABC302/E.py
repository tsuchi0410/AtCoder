N, Q = map(int,input().split())
G = [set() for _ in range(N)]
ans = N
for _ in range(Q):
    op = list(map(int,input().split()))
    if op[0] == 1:
        num, u, v = op
        u -= 1
        v -= 1
        if len(G[u]) == 0:
            ans -= 1
        if len(G[v]) == 0:
            ans -= 1
        G[u].add(v)
        G[v].add(u)
    else:
        num, v = op
        v -= 1
        if len(G[v]) > 0:
            ans += 1
            for u in G[v]:
                G[u].remove(v)
                if len(G[u]) == 0:
                    ans += 1
        G[v] = set()

    print(ans)