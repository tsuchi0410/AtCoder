# https://algo-method.com/tasks/312
N, M, K = map(int,input().split())
A = []
B = []
for i in range(N):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)
dp = [[False] * (M + 1) for _ in range(N)]
for i in range(N):
    for j in range(M + 1):
        if j == A[i]:
            dp[i][j] = 1
        if i == N - 1:
            break
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        if j + A[i + 1] < M + 1:
            dp[i + 1][j + A[i + 1]] = min(dp[i + 1][j + A[i + 1]], dp[i][j] + 1)
print("No") if dp[-1][-1] > K else print("Yes")


17
3, 5, 8
3, 2, 2

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ,,]
[3, ]