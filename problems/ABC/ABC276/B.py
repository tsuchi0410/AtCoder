n, m = (int(x) for x in input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
    a, b = (int(x) for x in input().split())
    # 有向グラフ
    g[a].append(b)
    # 無向グラフ
    g[b].append(a)

g = g[1:]
for i in range(len(g)):
    g[i].sort()

for i in range(len(g)):
    print(len(g[i]), *g[i])

