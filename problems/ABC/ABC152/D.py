from collections import defaultdict

N = int(input())

D = defaultdict(list)
for i in range(1, N + 1):
    A = str(i)   
    D[(A[0], A[-1])].append(i)

ans = 0
for k, v in D.items():
    if (k[1], k[0]) in D:
        ans += len(v) * len(D[(k[1], k[0])])

print(ans)