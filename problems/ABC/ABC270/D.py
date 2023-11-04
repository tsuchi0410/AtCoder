n, k = (int(x) for x in input().split())
a = list(map(int,input().split()))

dp = [[0]*(n+1) for _ in range(2)]
# 0:先手, 1:後手
for i in range(2):
    for j in range(n+1):
        for k in a:
            if j - k < 0:
                continue
            if i == 0:
                dp[1][j] = max(dp[1][j], j - dp[1][j-k])
            elif i == 1:
                dp[0][j] = max(dp[0][j], j - dp[0][j-k])

print(dp[0][-1])