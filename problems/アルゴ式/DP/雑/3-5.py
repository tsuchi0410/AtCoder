N,M = (int(x) for x in input().split())
W = list(map(int,input().split()))

dp = []
inf = 10000000
for i in range(N+1):
    dp.append([inf]*(M+1))

dp[0][0] = 0
for i in range(N):
    for j in range(M+1):
        if dp[i][j] == -1:
            continue

        dp[i+1][j] = min(dp[i][j], dp[i+1][j])

        if j+W[i] <= M:
            dp[i+1][j+W[i]] = dp[i][j] + 1


print(dp[-1][-1] if dp[-1][-1] != inf else "-1")
        

