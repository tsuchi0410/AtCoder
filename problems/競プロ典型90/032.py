n = int(input())
a = []
for i in range(n):
    aa = list(map(int,input().split()))
    a.append(aa)

import itertools
from collections import defaultdict
# 順列
l = list(range(n))
run = list(itertools.permutations(l))

m = int(input())
h = defaultdict(set)
for i in range(m):
    x,y = (int(x) for x in input().split())
    h[x-1].add(y-1)
    h[y-1].add(x-1)

ans = float('inf')
for i in run:
    f = 1
    time = 0
    for j in range(n):
        if j == n-1:
            time += a[i[j]][j]
            break
        if i[j] in h[i[j+1]]:
            f = 0
            break
        else:
            time += a[i[j]][j]

    if f == 1:
        ans = min(ans, time)

if ans == float('inf'):
    print('-1')
else:
    print(ans)