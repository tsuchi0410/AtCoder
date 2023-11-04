from collections import defaultdict
n, k = list(map(int,input().split()))
a = list(map(int,input().split()))

ans = 1
le = 0; ri = 0
d = defaultdict(int)
for ri in range(n):
    d[a[ri]] += 1
    if len(d) > k:
        while len(d) > k:
            d[a[le]] -= 1
            if d[a[le]] == 0:
                del d[a[le]]
            le += 1
    ans = max(ans, ri-le+1)
print(ans)