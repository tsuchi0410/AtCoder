from collections import deque
from collections import defaultdict

n = int(input())
l = defaultdict(list)
for i in range(n):
    a, b = (int(x) for x in input().split())
    l[a].append(b); l[b].append(a)

def bfs(u):
    queue = deque([u])
    S = set(); S.add(u)
    while queue:
        v = queue.popleft()
        for i in l[v]:
            if not i in S:
                queue.append(i)
                S.add(i)
    return S

a = bfs(1)

print(max(a))



