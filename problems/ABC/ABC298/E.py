N, A, B, P, Q = map(int, input().split())
MOD = 998244353

inv = pow(P, MOD - 2, MOD)
play = (1 * inv) % MOD
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][A] = 1
for i in range(N):
    for j in range(A, N):
        if dp[i][j] == 0:
            continue
        for k in range(P):
            nj = min(j + k + 1, N)
            dp[i + 1][nj] = dp[i][j] * inv
            dp[i + 1][nj] %= MOD

# 高橋君が 0 ターン以内でゴール、 1 ターン以内でゴール...
takahashi = []
for i in range(N + 1):
    takahashi.append(dp[i][-1])

inv = pow(Q, MOD - 2, MOD)
play = (1 * inv) % MOD
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][B] = 1
for i in range(N):
    for j in range(B, N):
        if dp[i][j] == 0:
            continue
        for k in range(Q):
            nj = min(j + k + 1, N)
            dp[i + 1][nj] = dp[i][j] * inv
            dp[i + 1][nj] %= MOD

ans = 0
for i in range(N + 1):
    T = 0
    for j in range(i + 1):
        T += takahashi[j]
        T %= MOD
    ans += dp[i][-1] * T
    ans %= MOD

print(ans)