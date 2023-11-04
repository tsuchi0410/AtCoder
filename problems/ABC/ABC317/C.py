import itertools

N, M = map(int, input().split())
A = [0] * M
B = [0] * M
C = [0] * M
G = [set() for _ in range(N)]
mp = {}
for i in range(M):
    A[i], B[i], C[i] = map(int, input().split())
    A[i] -= 1
    B[i] -= 1
    G[A[i]].add(B[i])
    G[B[i]].add(A[i])
    mp[(A[i], B[i])] = C[i]
    mp[(B[i], A[i])] = C[i]

ans = 0
city = list(range(N))
lst = list(itertools.permutations(city, N))
for citys in lst:
    v = citys[0]
    cnt = 0
    for j in range(1, len(citys)):
        nv = citys[j]
        f = False
        if nv in G[v]:
            cnt += mp[(v, nv)]
            v = nv
            f = True
        if f == False:
            break
    ans = max(ans, cnt)
print(ans)