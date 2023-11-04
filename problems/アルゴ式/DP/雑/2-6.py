N = int(input())

dp = []
A = []
for i in range(N):
    dp.append([0]*N)
    A.append(list(map(int,input().split())))

dp[0][0] = A[0][0]
for i in range(N):
    for j in range(N):
        if i-1 >= 0:
            dp[i][j] = max(dp[i-1][j] + A[i][j], dp[i][j])
        if j-1 >= 0:
            dp[i][j] = max(dp[i][j-1] + A[i][j], dp[i][j])


print(dp)
print(dp[-1][-1])