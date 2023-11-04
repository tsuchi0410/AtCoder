n, k = (int(x) for x in input().split())
a = list(map(int,input().split()))

if k >= n:
    l = [0]*n
    print(*l)
else:
    l2 = [0] * (k)
    l = a[k:] + l2
    print(*l)