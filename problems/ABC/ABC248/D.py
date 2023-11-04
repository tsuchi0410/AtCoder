from collections import defaultdict
import bisect
n = int(input())
a = list(map(int,input().split()))

d = defaultdict(list)
for i in range(n):
    d[a[i]].append(i)

q = int(input())
for i in range(q):
    qu = list(map(int,input().split()))
    l = qu[0]; r = qu[1]; num = qu[2]
    idxl = bisect.bisect_left(d[num], l-1)
    idxr = bisect.bisect_left(d[num], r)
    print(idxr - idxl)

