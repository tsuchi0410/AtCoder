import bisect
from collections import defaultdict
n = int(input())
a = list(map(int,input().split()))

d = defaultdict(int)
for i in range(n):
    d[a[i]] += 1

a = (n * (n-1) * (n-2)) / 6

b = 0
for i in d:
    if d[i] >= 3:
        b += (d[i] * (d[i]-1) * (d[i]-2)) / 6
    if d[i] >= 2:
        b += ((d[i] * (d[i]-1)) / 2) * (n - d[i])

print(int(a - b))

