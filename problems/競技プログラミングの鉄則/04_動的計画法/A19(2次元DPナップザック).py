N, W = map(int,input().split())
w = []
v = []
for _ in range(N):
    ww, vv = map(int,input().split())
    w.append(ww)
    v.append(vv)

dp = [[-1] * (W + 1) for _ in range(N)]

for i in range(N):
    for j in range(W + 1):
        
        # set
        if w[i] == j:
            dp[i][j] = max(dp[i][j], v[i])
        
        # check
        if i == N - 1:
            continue

        if dp[i][j] >= 1:
            # under
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            # next
            if j + w[i+1] < W + 1:
                dp[i+1][j+w[i+1]] = max(dp[i+1][j+w[i+1]], dp[i][j] + v[i+1])

print(max(dp[N-1]))