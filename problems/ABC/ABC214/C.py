N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

dp = [0] * N
dp[0] = T[0]
for i in range(N - 1):
    if S[i] + dp[i] > T[i + 1]:
        dp[i + 1] = T[i + 1]
    else:
        dp[i + 1] = S[i] + dp[i]

if dp[0] > dp[N - 1] + S[N - 1]:
    dp[0] = dp[N - 1] + S[N - 1]
    for i in range(N - 1):
        if S[i] + dp[i] > T[i + 1]:
            dp[i + 1] = T[i + 1]
        else:
            dp[i + 1] = S[i] + dp[i]

print(*dp, sep = "\n")