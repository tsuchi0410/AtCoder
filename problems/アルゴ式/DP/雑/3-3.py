N, M = (int(x) for x in input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dp = []
for i in range(N):
    dp.append([-1]*M)

dp[0][0] = 0
for i in range(0,N-1):
    for j in range(0,M):
        # スキップ
        if dp[i][j] < 0:
            continue

        # 下
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])

        # 右下
        if j+A[i] < M:
            dp[i+1][j+A[i]] = max(dp[i+1][j+A[i]], dp[i][j] + B[i])
        
print(dp[-1][-1])  

  




    




