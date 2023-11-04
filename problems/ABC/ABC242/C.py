N = int(input())

dp = []
for i in range(N):
    if i == 0:
        dp.append([1]* 9)
    else:
        dp.append([0] * 9)

for i in range(N-1):
    for j in range(9):
        
        if j == 0:
            dp[i+1][j] += dp[i][j]
            dp[i+1][j+1] += dp[i][j]
        
        elif j == 8:
            dp[i+1][j] += dp[i][j]
            dp[i+1][j-1] += dp[i][j] 
        
        else:
            dp[i+1][j-1] += dp[i][j]
            dp[i+1][j] += dp[i][j]
            dp[i+1][j+1] += dp[i][j]
            
        dp[i+1][j] %= 998244353


print(int(sum(dp[-1])%998244353))