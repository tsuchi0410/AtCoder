N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

dp = [0] * N
S = [0] * (N + 1)
for i in range(N - 2, -1, -1):
    dp[i] += A[i] + 1
    dp[i] += S[i + 1] - S[i + A[i] + 1] 
    dp[i] %= MOD
    inv = pow(A[i], MOD - 2, MOD)
    play = (1 * inv) % MOD
    dp[i] *= play
    dp[i] %= MOD
    S[i] = dp[i] + S[i + 1]
    S[i] %= MOD

print(dp[0])