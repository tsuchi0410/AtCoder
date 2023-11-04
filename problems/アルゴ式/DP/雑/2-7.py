N = int(input())

A = []
dp = []
for i in range(N):
    A.append(list(map(int,input().split())))
    dp.append([10000000000]*N)

dp[0][N-1] = A[0][N-1]
for i in range(N):
    for j in range(N-1,-1,-1):
        if i-1 >= 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j]+A[i][j])
        if N-1 > j:
            dp[i][j] = min(dp[i][j], dp[i][j+1]+A[i][j])

print(dp[N-1][0])