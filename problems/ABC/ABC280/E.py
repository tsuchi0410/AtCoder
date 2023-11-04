N, P = map(int, input().split())
MOD = 998244353
inv100 = pow(100, MOD - 2, MOD)
p = P * inv100 % MOD

dp = [0] * (N + 1)
dp[1] = 1
for i in range(2, N + 1):
    dp[i] = 1 + p * dp[i - 2] % MOD + (1 - p) * dp[i - 1] % MOD
    dp[i] %= MOD
print(dp[N])