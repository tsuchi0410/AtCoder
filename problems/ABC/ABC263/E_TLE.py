N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

dp = [0] * N
for i in range(N - 2, -1, -1):
    dp[i] += A[i] + 1
    for j in range(1, A[i] + 1):
        dp[i] += dp[i + j]
        dp[i] %= MOD
    inv = pow(A[i], MOD - 2, MOD)
    play = (1 * inv) % MOD
    dp[i] *= play
    dp[i] %= MOD

print(dp)