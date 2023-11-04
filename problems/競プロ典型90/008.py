n = int(input())
s = input()
mod = 10 ** 9 + 7
l = 'atcoder'
dp = [[0] * (n+1) for _ in range(len(l))]

for i in range(len(l)):
    c = l[i]
    for j in range(1, n+1):
        if i == 0:
            if s[j-1] == c:
                dp[i][j] = dp[i][j-1] + 1
            else:
                dp[i][j] = dp[i][j-1]
            continue

        if s[j-1] == c:
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1] 
        else:
            dp[i][j] = dp[i][j-1]

        dp[i][j] %= mod

print(dp[-1][-1] % mod)