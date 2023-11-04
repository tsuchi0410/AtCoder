N = int(input())
dp = [[[] for _ in range(6)] for _ in range(N)]
for i in range(6):
    dp[0][i] = i + 1
for i in range(1, N):
    E = 0
    for j in range(6):
        E += dp[i - 1][j]
    E /= 6
    for j in range(6):
        dp[i][j] = max(dp[i - 1][j], E)

ans = 0
for i in range(6):
    ans += dp[N - 1][i]
print(ans / 6)