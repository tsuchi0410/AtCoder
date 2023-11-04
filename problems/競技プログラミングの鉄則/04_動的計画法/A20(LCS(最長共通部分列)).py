S = input()
T = input()
M = len(S)
N = len(T)
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        if T[i] == S[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
print(dp[-1][-1])