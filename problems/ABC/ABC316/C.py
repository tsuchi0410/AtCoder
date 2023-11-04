from collections import defaultdict
from sortedcontainers import SortedList
N = int(input())
d = defaultdict(SortedList)
for i in range(N):
    F, S = map(int, input().split())
    d[F].add(S)

L = []
# 1 個ずつ
ans = 0
if len(d) >= 2:
    for k, v in d.items():
        L.append(v[-1])
    L.sort()
    ans = L[-1] + L[-2]

for k, v in d.items():
    if len(v) >= 2:
        num = v[-1] + v[-2] // 2
        ans = max(ans, num)

print(ans)
