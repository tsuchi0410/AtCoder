N = int(input())

dp = []
buf = []
for i in range(N):
    S = str(input())
    for j in range(N):
        if S[j] == ".":
            buf.append(0)
        else:
            buf.append("nan")
    dp.append(buf)
    buf = []

dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if dp[i][j] != "nan":
            if i >= 0 and dp[i-1][j] != "nan":
                dp[i][j] += dp[i-1][j]
            if j >= 0 and dp[i][j-1] != "nan":
                dp[i][j] += dp[i][j-1]

print(dp[-1][-1])