from collections import defaultdict
N, M = map(int,input().split())
G = defaultdict(int)
for i in range(M):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    if a < b:
        G[b] += 1
    elif b < a:
        G[a] += 1
ans = 0
for k, v in G.items():
    if v == 1:
        ans += 1
print(ans)
