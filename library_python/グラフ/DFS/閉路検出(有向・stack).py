N, M = int(input())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)

seen = [False] * N
stack = [0]  # スタート
history = []
cycle = []
while len(stack):
    v = stack.pop()
    if seen[v] == True:
        cycle_start = history.index(v)
        cycle = history[cycle_start:]
        break
    seen[v] = True
    history.append(v)
    for u in G[v]:
        stack.append(u)

print(cycle)
