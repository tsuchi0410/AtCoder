N = int(input())
W = list(map(int,input().split()))

dp = []
INF = 10000000000
wmax = 1000*50*2+1
for i in range(N+1):
    dp.append([0]*wmax+[0])

dp[0][int(wmax/2)] = INF
for i in range(N):
    for j in range(wmax):
        # 存在確認
        if dp[i][j] == 0:
            continue

        dp[i+1][j] = min(dp[i][j], dp[i+1][j])

        # 左側
        if  j-W[i] >= 0: 
            dp[i+1][j-W[i]] = 1
        # 右側
        if j+W[i] < wmax:
            dp[i+1][j+W[i]] = 1

ans = INF
for judge in range(wmax):
    if dp[-1][judge] == 1:
        ans = min(ans, abs(int(wmax/2)-judge))

print(ans)


