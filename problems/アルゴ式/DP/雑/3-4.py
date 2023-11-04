N,M = (int(x) for x in input().split())
W = list(map(int,input().split()))
V = list(map(int,input().split()))

dp = []
for i in range(N+1):
    dp.append([-1]*(M+1))

dp[0][0] = 0
for i in range(N):
    for j in range(M+1):
        if dp[i][j] < 0:
            continue

        dp[i+1][j] = max(dp[i][j], dp[i+1][j])

        if j+W[i] <= M:
            dp[i+1][j+W[i]] = max(dp[i+1][j+W[i]], dp[i][j] + V[i])

print(dp)
print(max(dp[N]))
