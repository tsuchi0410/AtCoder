from collections import deque
MOD = 998244353

N, M, K = map(int, input().split())
bad = []
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    bad.append([u, v])
    bad.append([v, u])

dp = [[0] * N for _ in range(K)]
dp[0][0] = 1
for i in range(K - 1):
    cnt = sum(dp[i])
    for j in range(N):
        dp[i + 1][j] = cnt - dp[i][j]
    for u, v in bad:
        dp[i + 1][u] -= dp[i][v]
    for j in range(N):
        dp[i + 1][j] %= MOD

ans = 0
for i in range(1, N):
    ans += dp[-1][i]
for u, v in bad:
    if v == 0:
        ans -= dp[-1][u]

print(ans % MOD)