from collections import defaultdict

N, K = (int(x) for x in input().split())
a = list(map(int,input().split()))

d = defaultdict(list)
for i in range(N):
    d[i % K].append(a[i])

a2 = sorted(a)
d2 = defaultdict(list)
for i in range(N):
    d2[i % K].append(a2[i])
    
for i in range(len(d)):
    d[i] = sorted(d[i])
    d2[i] = sorted(d2[i])
    
    if d[i] != d2[i]:
        print('No')
        exit()

print('Yes')