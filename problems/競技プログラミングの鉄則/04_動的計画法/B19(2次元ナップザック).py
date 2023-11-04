N, W = map(int,input().split())
w = []
v = []
for _ in range(N):
    ww, vv = map(int,input().split())
    w.append(ww)
    v.append(vv)

INF = 10 ** 18
val = 1000 * 101
dp = [[INF] * (val) for _ in range(N+1)]

for i in range(N+1):
    dp[i][0] = 0

for i in range(1, N+1):
    for j in range(val):
        # set
        if j == v[i-1]:
            dp[i][j] = min(dp[i][j], w[i-1])
        
        # check
        if i == N:
            continue
        
        if dp[i][j] != INF:
            # under
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            # next
            if dp[i][j] + w[i] <= W:
                dp[i+1][j+v[i]] = min(dp[i+1][j+v[i]], dp[i][j] + w[i])

ans = 0
for i in range(N+1):
    for j in range(val):
        if dp[i][j] != INF:
            ans = max(ans, j)
print(ans)