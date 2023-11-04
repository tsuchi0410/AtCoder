n = int(input())
l = list(map(int,input().split()))

inf = 21
dp = [[0] * inf for _ in range(n-1)]

# 初期値
dp[0][l[0]] = 1
for i in range(n-1):
    for j in range(inf):
        
        if i == n-2:
            continue
        
        if dp[i][j] > 0:
            if j + l[i+1] < inf:
                dp[i+1][j+l[i+1]] += dp[i][j]
            if j - l[i+1] >= 0:
                dp[i+1][j-l[i+1]] += dp[i][j]

print(dp[-1][l[-1]])
