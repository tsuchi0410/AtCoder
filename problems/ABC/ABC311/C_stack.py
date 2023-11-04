N = int(input())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for i in range(N):
    G[i].append(A[i] - 1)

seen = [False] * N
for i in range(N):
    if seen[i] == False:
        stack = [i]
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
    
    if len(cycle) != 0:
        break

print(len(cycle))
for i in range(len(cycle)):
    cycle[i] += 1
print(*cycle)
