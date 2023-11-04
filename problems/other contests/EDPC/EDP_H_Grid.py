MOD = 10 ** 9 + 7
H, W = map(int, input().split())
S = [input() for _ in range(H)]
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            if j + 1 < W and S[i][j + 1] == ".":
                dp[i][j + 1] += dp[i][j]
                dp[i][j + 1] %= MOD
            if i + 1 < H and S[i + 1][j] == ".":
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= MOD

print(dp[-1][-1])