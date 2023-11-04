import bisect
from collections import defaultdict

h, w, rs, cs = (int(x) for x in input().split())
n = int(input())
rc = []
for i in range(n):
    r, c = (int(x) for x in input().split())
    rc.append([r, c])
q = int(input())
dl = []
for i in range(q):
    d, l = (x for x in input().split())
    dl.append([d, int(l)])


d1 = defaultdict(list)
d2 = defaultdict(list)
for i in rc:
    d1[i[0]].append(i[1])
    d2[i[1]].append(i[0])

for i in d1:
    d1[i] = sorted(d1[i])

for i in d2:
    d2[i] = sorted(d2[i])

print(d1)
print(d2)

print(d1[3][1])