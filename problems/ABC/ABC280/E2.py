N, P = map(int, input().split())
MOD = 998244353
inv100 = pow(100, MOD - 2, MOD)
critical = (P * inv100) % MOD
normal = ((100 - P) * inv100) % MOD
dp = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = (dp[max(0, i - 2)] + 1) * critical + (dp[i - 1] + 1) * normal
    dp[i] %= MOD
print(dp[-1])