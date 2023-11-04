import itertools
N, M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

ans = 0
lst = list(itertools.permutations(list(range(N)), N))
for vs in lst:
    if vs[0] != 0:
        continue
    else:
        flag = True
        for i in range(N - 1):
            v = vs[i]
            next = vs[i + 1]
            if next in G[v]:
                continue
            else:
                flag = False
                break 
        if flag == True:
            ans += 1
print(ans)