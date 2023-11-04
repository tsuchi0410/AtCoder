mod = 10 ** 9 + 7
n, l = (int(x) for x in input().split())
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, len(dp)):
    dp[i] = dp[i-1]
    if i >= l:
        dp[i] += dp[i - l]
    dp[i] %= mod

print(dp[-1])
