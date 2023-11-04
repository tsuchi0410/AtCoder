from collections import defaultdict, deque, Counter

def euler_tour(G, root=0):
    n = len(G)
    euler = []
    dq = deque([root])
    dq2 = deque()
    visited = [0] * n
    while dq:
        u = dq.pop()
        euler += [u]
        if visited[u]:
            continue
        for v in reversed(G[u]):
            if visited[v]:
                dq += [v]
            # [親頂点、子頂点、子頂点、。。。]と入れていく.その後連結
            else:
                dq2 += [v]
        dq.extend(dq2)
        dq2 = deque()
        visited[u] = 1
    return euler

N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

for v in range(N):
    G[v].sort()

res = euler_tour(G, 0)

ans = []
for i in range(len(res)):
    ans.append(res[i] + 1)
print(*ans)