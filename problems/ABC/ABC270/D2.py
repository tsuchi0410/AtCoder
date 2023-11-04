N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * (N + 1)
for n in range(1, N + 1):
    for a in A:
        if n - a < 0:break
        dp[n] = max(dp[n], n - dp[n - a])

print(dp[N])
print(dp)