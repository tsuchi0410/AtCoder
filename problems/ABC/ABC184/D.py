A, B, C = map(int, input().split())
N = 101
dp = [[[0] * N for _ in range(N)] for _ in range(N)]
for i in range(N - 1, -1, -1):
    for j in range(N - 1, -1, -1):
        for k in range(N - 1, -1, -1):
            if i == 100 or j == 100 or k == 100:
                continue
            if i + j + k == 0:
                continue
            dp[i][j][k] += (i / (i + j + k)) * (dp[i + 1][j][k] + 1)
            dp[i][j][k] += (j / (i + j + k)) * (dp[i][j + 1][k] + 1)
            dp[i][j][k] += (k / (i + j + k)) * (dp[i][j][k + 1] + 1)

print(dp[A][B][C])