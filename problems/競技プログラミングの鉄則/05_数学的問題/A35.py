N = int(input())
A = list(map(int, input().split()))
dp = []
for i in range(N):
    dp.append([0] * (i + 1))
for i in range(N):
    dp[-1][i] = A[i]
for i in range(N - 2, -1, -1):
    for j in range(len(dp[i])):
        if i % 2 == 0:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])
        else:
            dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1])
print(dp[0][0])