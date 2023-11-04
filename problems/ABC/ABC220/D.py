n =int(input())
a = list(map(int,input().split()))
mod = 998244353

dp = [[0] * 10 for _ in range(n)]
dp[0][a[0]] = 1

for i in range(n):
    for j in range(10):
        dp[i][j] %= mod
        if i == n-1:
            continue
        if dp[i][j] > 0:
            dp[i+1][(j+a[i+1])%10] += dp[i][j]
            dp[i+1][(j*a[i+1])%10] += dp[i][j]
            
for i in dp[-1]:
    print(i%mod)
