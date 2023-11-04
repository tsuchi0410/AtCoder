n = int(input())
x, y = (int(x) for x in input().split())
ab = []
for i in range(n):
    a, b = (int(x) for x in input().split())
    ab.append([a, b])

dp = [[[float('inf')] * (y+1) for _ in range(x+1)] for _ in range(301)]
dp[0][0][0] = 0
for i in range(n):
    for j in range(x+1):
        jj = min(j+ab[i][0], x)
        for k in range(y+1):
            if dp[i][j][k] < float('inf'):
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                kk = min(k+ab[i][1], y)
                dp[i+1][jj][kk] = min(dp[i+1][jj][kk], dp[i][j][k] + 1)

if dp[n][-1][-1] == float('inf'):
    print(-1)
else:
    print(dp[n][-1][-1])