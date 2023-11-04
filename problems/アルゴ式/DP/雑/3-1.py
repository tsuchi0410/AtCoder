N, M = (int(x) for x in input().split())
A = list(map(int,input().split()))

dp = []
for i in range(N):
    dp.append([0]*M)

dp[0][0] = 1
c = 0
for i in range(1, N):
    for j in range(M):
        if dp[i-1][j] == 1:
            dp[i][j] = 1 
        if j-A[i-1] >= 0 and dp[i-1][j-A[i-1]] == 1:
            dp[i][j] = 1
        if i == N-1 and dp[i][j] == 1:
            c += 1

print(c)
