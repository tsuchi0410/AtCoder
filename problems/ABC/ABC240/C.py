from collections import defaultdict
n, x = map(int, input().split())
d = defaultdict(set)
for i in range(n):
    a, b = map(int, input().split())
    if i == 0:
        d[i].add(a)
        d[i].add(b)
    else:
        for j in d[i-1]:
            d[i].add(a + j)
            d[i].add(b + j)

if x in d[n-1]:
    print('Yes')
else:
    print('No')
