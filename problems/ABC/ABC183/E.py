MOD = 10**9 + 7
H, W = map(int, input().split())
S = [input() for _ in range(H)]

dp = [[0] * W for _ in range(H)]
X = [[0] * (W + 1) for _ in range(H + 1)]
Y = [[0] * (W + 1) for _ in range(H + 1)]
Z = [[0] * (W + 1) for _ in range(H + 1)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        if j - 1 >= 0:
            X[i][j] = X[i][j - 1] + dp[i][j - 1]
        if i - 1 >= 0:
            Y[i][j] = Y[i - 1][j] + dp[i - 1][j]
        if j - 1 >= 0 and i - 1 >= 0:
            Z[i][j] = Z[i - 1][j - 1] + dp[i - 1][j - 1]
        dp[i][j] += X[i][j] + Y[i][j] + Z[i][j]
        dp[i][j] %= MOD
 
print(dp[-1][-1])