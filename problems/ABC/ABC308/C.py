from collections import defaultdict
import decimal
N = int(input())
L = []
for i in range(N):
    A, B = map(int, input().split())
    p = decimal.Decimal(str(A)) / decimal.Decimal(str(A + B))
    L.append([p, i + 1])
L.sort(reverse=True)

ans = defaultdict(list)
for k, v in L:
    ans[k].append(v)

a = []
for k, v in ans.items():
    if len(v) >= 2:
        v2 = sorted(v)
        a += v2
    else:
        a += v
print(*a)
