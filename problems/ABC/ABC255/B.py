def d(xa, ya, xb, yb):
    return ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5

N, K = map(int,input().split())
A = list(map(int,input().split()))
L = []
for _ in range(N):
    x, y = map(int,input().split())
    L.append([x, y])

ans = 0
for y, x in L:
    cnt = 10 ** 18
    for i in A:
        i -= 1
        y2, x2 = L[i]
        cnt = min(cnt, d(x, y, x2, y2))
    ans = max(ans, cnt)

print(ans)