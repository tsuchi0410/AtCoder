MOD = 998244353

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0, 0] for _ in range(N+1)]
dp[1][0] = 1

for i in range(2, N+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
    dp[i][1] = dp[i-1][0]

ans = dp[N][0] + dp[N][1]
for i in range(1, N):
    if A[i] != A[i-1] and B[i] != B[i-1]:
        ans = (ans - dp[i][1] * dp[N-i][0]) % MOD

print(ans)