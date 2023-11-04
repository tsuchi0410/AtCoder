n, k, p = (int(x) for x in input().split())
a = list(map(int,input().split()))

a1 = a[:n//2]
a2 = a[n//2:]

table = []
for i in range(2 ** n1):
    l = [i >> j & 1 for j in range(n)]
    for j in range(len(l)):
        if l[j] == 1: