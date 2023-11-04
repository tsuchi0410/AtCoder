import itertools
n, m = (int(x) for x in input().split())
kx = []
for i in range(m):
    kx.append(list(map(int,input().split())))

a = list(range(n))
for i in range(n):
    a[i] += 1

l = list(itertools.combinations(a, 2))

d = {}
for i in range(len(l)):
    d[l[i]] = 1

c = []
for i in range(m):
    
    l2 = list(itertools.combinations(kx[i][1:], 2))
    for i in l2:
        d[i] = 0

for i in d:
    if d[i] == 1:
        print('No')
        exit()


print('Yes')
