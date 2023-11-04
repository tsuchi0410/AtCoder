N, M, K = map(int, input().split())

MOD = 998244353
inv = pow(M, MOD - 2, MOD)
play = (1 * inv) % MOD
dp = [[0] * (N + 1) for _ in range(K + 1)]
dp[0][0] = 1

for i in range(K):
    for j in range(N):
        if dp[i][j] == 0:
            continue
        for k in range(M):
            if j + k + 1 <= N:
                dp[i + 1][j + k + 1] += dp[i][j] * play
                dp[i + 1][j + k + 1] %= MOD
            else:
                dp[i + 1][N - (j + M - N)] += dp[i][j] * play
                dp[i + 1][N - (j + M - N)] %= MOD

ans = 0
for i in range(K + 1):
    ans += dp[i][-1]
    ans %= MOD
print(ans)
