N = int(input())
S = input()
dp = [[0] * 2 for _ in range(N)]
ans = 0
for i in range(N):
    if int(S[i]) == 0:
        dp[i][0] += 1
    elif int(S[i]) == 1:
        dp[i][1] += 1
    
    if i == N - 1:
        ans += dp[i][1]
        continue

    if int(S[i + 1]) == 0:
        dp[i + 1][1] += dp[i][0]
        dp[i + 1][1] += dp[i][1]
    elif int(S[i + 1]) == 1:
        dp[i + 1][0] += dp[i][1]
        dp[i + 1][1] += dp[i][0]
    
    ans += dp[i][1]

print(ans)