# https://algo-method.com/tasks/310
N, M = map(int,input().split())
A = list(map(int,input().split()))
dp = [[0] * (M + 1) for _ in range(N)]
for i in range(N):
    for j in range(M + 1):
        if j == A[i]:
            dp[i][j] += 1
        if i == N - 1:
            break
        if dp[i][j] > 0:
            dp[i + 1][j] += dp[i][j]
        if dp[i][j] > 0 and j + A[i + 1] < M + 1:
            dp[i + 1][j + A[i + 1]] += dp[i][j]
print(dp[-1][-1])