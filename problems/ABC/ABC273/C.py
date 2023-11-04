from collections import defaultdict
import bisect

n = int(input())
a = list(map(int,input().split()))

a2 = list(set(a))
a2 = sorted(a2)

d = defaultdict(int)
for i in range(n):
    d[i] = 0

for i in range(n):
    
    idx = bisect.bisect_left(a2, a[i])
    d[len(a2) - (idx+1)] += 1

    
for i in d:
    print(d[i])
    