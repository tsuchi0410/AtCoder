# https://algo-method.com/tasks/308
N, W = map(int,input().split())
w = []
v = []
for _ in range(N):
    ww, vv = map(int,input().split())
    w.append(ww)
    v.append(vv)
dp = [[0] * (W + 1) for _ in range(N)]
for i in range(N):
    for j in range(W + 1):
        if j == w[i]:
            dp[i][j] = max(dp[i][j], v[i])
        if i == N - 1:
            break
        if dp[i][j] > 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if dp[i][j] > 0 and j + w[i + 1] < W + 1:
            dp[i + 1][j + w[i + 1]] = max(dp[i + 1][j + w[i + 1]], dp[i][j] + v[i + 1])
print(max(dp[-1]))