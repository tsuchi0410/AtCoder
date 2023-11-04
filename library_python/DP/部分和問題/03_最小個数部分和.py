# https://algo-method.com/tasks/311
N, M = map(int,input().split())
A = list(map(int,input().split()))
INF = 10**18
dp = [[INF] * (M + 1) for _ in range(N)]
for i in range(N):
    for j in range(M + 1):
        if j == A[i]:
            dp[i][j] = 1
        if i == N - 1:
            break
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        if j + A[i + 1] < M + 1:
            dp[i + 1][j + A[i + 1]] = min(dp[i + 1][j + A[i + 1]], dp[i][j] + 1)
print(-1) if dp[-1][-1] == INF else print(dp[-1][-1])