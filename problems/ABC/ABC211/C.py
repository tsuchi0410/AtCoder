S = str(input())

q = "chokudai"
dp = []
for i in range(8):
    dp.append([0]*len(S))


# 1段目
if q[0] == S[0]:
    dp[0][0] = 1

for j in range(1,len(S)):
    if q[0] == S[j]:
        dp[0][j] = dp[0][j-1] + 1
    else:
        dp[0][j] = dp[0][j-1]



# 2段目以降
for i in range(1,8):
    for j in range(len(S)):

        if i-1 >= j:
            dp[i][j] = 0
            continue
        
        if q[i] == S[j]:
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
        else:
             dp[i][j] = dp[i][j-1]

print(dp[-1][-1] % (10**9 + 7))
    
