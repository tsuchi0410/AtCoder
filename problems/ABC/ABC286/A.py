n,p,q,r,s = (int(x) for x in input().split())
a = list(map(int,input().split()))
pq = a[p-1:q]
rs = a[r-1:s]

b = []
i = 0
while i < n:
    if i == p-1:
        for j in range(len(rs)):
            b.append(rs[j])
        i += len(rs)

    elif i == r-1:
        for j in range(len(pq)):
            b.append(pq[j])
        i += len(pq)
    else:
        b.append(a[i])
        i += 1

print(*b)