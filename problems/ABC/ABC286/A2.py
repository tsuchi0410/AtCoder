n,p,q,r,s = (int(x) for x in input().split())
a = list(map(int,input().split()))
a[p-1:q], a[r-1:s] = a[r-1:s], a[p-1:q]
print(*a)