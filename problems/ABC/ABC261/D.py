from collections import defaultdict

N,M = (int(x) for x in input().split())
X = list(map(int,input().split()))
CY = defaultdict(int)
for i in range(M):
    x,y = (int(x) for x in input().split())
    CY[x] = y
    
dp = []
maxC = 5001
for i in range(N):
    dp.append([0] * maxC)


for i in range(N):
    for j in range(maxC):
        
        if 1 in CY:
            dp[i][1] = max(X[i] + CY[1], dp[i][1])
        else:
            dp[i][1] = max(X[i], dp[i][1])
        
        if i == N - 1:
            continue
        
        # next
        if dp[i][j] > 0:
            # 表
            if j+1 in CY:
                dp[i+1][j+1] += max(dp[i][j] + X[i+1] + CY[j+1], dp[i+1][j+1])
            else:
                dp[i+1][j+1] += max(dp[i][j] + X[i+1], dp[i+1][j+1])
                
            
        # 裏
        dp[i+1][0] = max(dp[i][j], dp[i+1][0])

print(max(dp[-1]))