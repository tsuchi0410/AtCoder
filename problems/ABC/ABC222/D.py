n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

inf = 3001
dp = []
for i in range(n):
    dp.append([0] * inf)
    
for i in range(n): 
    for j in range(inf):

        if j < a[i]:
            dp[i][j] = 0
        
        if i == n-1:
            continue
                
        # 初期値
        if i == 0:
            if j >= a[i] and b[i] >= j:
                dp[i][j] = 1
                
        if dp[i][j] > 0:
            dp[i+1][j] += dp[i][j] + dp[i+1][j-1]
        
        elif b[i+1] >= j:
            dp[i+1][j] = dp[i+1][j-1]
        
        dp[i+1][j] %= 998244353

print(sum(dp[-1]) % 998244353)
