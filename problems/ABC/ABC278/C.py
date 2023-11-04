from collections import defaultdict
n,q = (int(x) for x in input().split())

d = defaultdict(set)
for i in range(q):
    t,a,b = (int(x) for x in input().split())
    if t == 1:
        d[a].add(b)
    elif t == 2:
        if b in d[a]:
            d[a].remove(b)
    else:
        if b in d[a] and a in d[b]:
            print('Yes')
        else:
            print('No')