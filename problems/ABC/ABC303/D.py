X, Y, Z = map(int,input().split())
S = input()
N = len(S)
dp = [[0, 0] for _ in range(N + 1)]
dp[0][1] = 10 ** 18
for i in range(N):
    if S[i] == "a":
        dp[i + 1][0] = min(dp[i][0] + X, dp[i][1] + Z + X)
        dp[i + 1][1] = min(dp[i][1] + Y, dp[i][0] + Z + Y)
    elif S[i] == "A":
        dp[i + 1][0] = min(dp[i][0] + Y, dp[i][1] + Z + Y)
        dp[i + 1][1] = min(dp[i][1] + X, dp[i][0] + Z + X)
print(min(dp[-1]))
