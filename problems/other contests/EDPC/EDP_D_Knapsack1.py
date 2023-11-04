N, W = (int(x) for x in input().split())
w = []
v = []
dp = []
for i in range(N):
    a, b = (int(x) for x in input().split())
    w.append(a)
    v.append(b)
    dp.append([0] * (W+1))
    
for i in range(N):
    for j in range(W+1):
        
        # new
        if j == w[i]:
            dp[i][j] = max(dp[i][j], v[i])
            
        # end
        if i == N - 1:
            continue
            
        # under
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        
        # next
        if dp[i][j] > 0:
            if j + w[i+1] < W + 1:
                dp[i+1][j+w[i+1]] = max(dp[i+1][j], dp[i][j] + v[i+1])
            
print(max(dp[-1]))