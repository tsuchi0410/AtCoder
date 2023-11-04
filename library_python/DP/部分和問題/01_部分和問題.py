# https://algo-method.com/tasks/309
N, M = map(int,input().split())
A = list(map(int,input().split()))
dp = [[False] * (M + 1) for _ in range(N)]
for i in range(N):
    for j in range(M + 1):
        if j == A[i]:
            dp[i][j] = True
        if i == N - 1:
            break
        if dp[i][j] == True:
            dp[i + 1][j] = True
        if dp[i][j] == True and j + A[i + 1] < M + 1:
            dp[i + 1][j + A[i + 1]] = True
print("Yes") if dp[-1][-1] == True else print("No")