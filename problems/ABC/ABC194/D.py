N = int(input())
dp = [0] * (N)
for i in range(1, N):
    dp[i] = dp[i-1] + (1 / ((N - i) / N))

print(dp[-1])