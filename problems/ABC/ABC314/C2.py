from collections import deque
from collections import defaultdict

N, M = map(int, input().split())
S = list(input())
C = list(map(int, input().split()))

d = defaultdict(deque)
for i in range(N):
    d[C[i]].append(i)

ans = [0] * N
for k, v in d.items():
    q = deque([])
    for i in v:
        q.append(i)
    q.rotate()
    for i in range(len(v)):
        old = v.pop()
        new = q.pop()
        ans[old] = S[new]

print("".join(ans))