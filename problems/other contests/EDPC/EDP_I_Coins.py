N = int(input())
p = list(map(float, input().split()))
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if dp[i][j] == 0:
            continue
        # 裏
        dp[i + 1][j] += dp[i][j] * (1 - p[i])
        # 表
        dp[i + 1][j + 1] += dp[i][j] * p[i]

# for i in dp:
#     print(i)

ans = 0
for i in range(N + 1):
    if i >= (N + 1) // 2:
        ans += dp[N][i]
print(ans)

