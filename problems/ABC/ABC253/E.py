N, M, K = map(int, input().split())
MOD = 998244353
dp = [[0] * (M + 2) for _ in range(N)]
for i in range(1, M + 1):
    dp[0][i] += 1

for i in range(N - 1):
    cnt = sum(dp[i])
    for j in range(1, K + 1):
        cnt -= dp[i][j]
    cnt %= MOD
    for j in range(1, M + 1):
        dp[i + 1][j] += cnt
        if j + 1 >= K:
            cnt += dp[i][j + 1 - K]
        if j + K <= M + 1:
            cnt -= dp[i][j + K]
    for j in range(1, M + 1):
        dp[i + 1][j] %= MOD


print(sum(dp[N - 1]) % MOD)