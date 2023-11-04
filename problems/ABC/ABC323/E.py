N, X = map(int, input().split())
T = list(map(int, input().split()))
MOD = 998244353
inv = pow(N, MOD - 2, MOD)
play = (1 * inv) % MOD

dp = [0] * (X + 1)
dp[0] = 1
ans = 0
for i in range(X + 1):
    if dp[i] == 0:
        continue
    for j in range(N):
        if i <= X and i + T[j] > X and j == 0:
            ans += dp[i] * play
            ans %= MOD
        if i + T[j] <= X:
            dp[i + T[j]] += dp[i] * play
            dp[i + T[j]] %= MOD

print(ans)